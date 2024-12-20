import datetime
from django.utils.datastructures import MultiValueDictKeyError

from django_instance.settings import JS_TIME_FORMAT
from schedule import models


# depricated(included in project_details (project returns with tasks)))
def get_all_tasks(project: models.Project):
    tasks = models.Task.objects.filter(project_instance=project)
    all_tasks = []
    for task in tasks:
        proj_dict = task.dict_with_convert_time_field_to_json()
        all_tasks.append(proj_dict)

    tasks_dict = {"tasks": all_tasks}
    return tasks_dict


def create_new_task(task_info: dict, project: models.Project):
    try:
        task_description = task_info["description"]
    except MultiValueDictKeyError:
        return {"error": "Bad POST", "status": 422}

    if task_description != "" and len(task_description) < 1000:
        priority = project.get_next_max_priority()

        new_task = models.Task.objects.create(
            project_instance=project,
            description=task_description,
            priority=priority,
        )
        try:
            expire_date = task_info["expire_date"]
        except MultiValueDictKeyError:
            expire_date = new_task.expire_date
        else:
            if expire_date == "" or expire_date == "None" or expire_date is None:
                expire_date = None
            else:
                expire_date = datetime.datetime.strptime(expire_date, JS_TIME_FORMAT)
                new_task.expire_date = expire_date

        new_task.save()
        return {"task": new_task.dict_with_convert_time_field_to_json()}
    else:
        return {"error": "Bad POST", "status": 422}


def get_task(task: models.Task):
    return task.dict_with_convert_time_field_to_json()


def edit_task(task: models.Task, task_info: dict):
    try:
        description = task_info["description"]
    except MultiValueDictKeyError:
        description = task.description
    else:
        if 0 < len(description) < 1000:
            task.description = description
        else:
            return {"error": "Bad POST", "status": 422}

    try:
        expire_date = task_info["expire_date"]
    except MultiValueDictKeyError:
        expire_date = task.expire_date
    else:
        if expire_date == "" or expire_date == "None" or expire_date is None:
            expire_date = None
        else:
            expire_date = datetime.datetime.strptime(expire_date, JS_TIME_FORMAT)
            task.expire_date = expire_date

    try:
        if task_info["is_completed"].lower() == "true" or task_info["is_completed"] == True: # noqa: E712 PLR0911
            is_completed = True
        else:
            is_completed = False

        task.is_completed = is_completed
    except MultiValueDictKeyError:
        pass

    task.save()
    return task.dict_with_convert_time_field_to_json()


def delete_task(task: models.Task) -> None:
    task_dict = task.dict_with_convert_time_field_to_json()
    task.delete()
    return task_dict
