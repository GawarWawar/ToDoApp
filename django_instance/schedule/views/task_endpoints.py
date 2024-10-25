from allauth.account import decorators

from django.http import QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from schedule import models
from .utils.task_actions import get_task, edit_task, delete_task


@decorators.login_required
@csrf_exempt
def task_endpoint(request, task_id):
    try:
        task = models.Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        context = {
            "error": "Bad ID",
            "meassage": "Please ensure that task with this id exists",
        }
        return render(request, "notify_form.html", context)

    if request.method == "GET":
        task_details = {"task": get_task(task)}
        return render(request, "task_id.html", context=task_details)

    elif request.method == "PUT":
        task_info = QueryDict(request.body)

        task_after_edit = edit_task(task, task_info)

        if task_after_edit.get("error", None) is None:
            return render(request, "task_id.html", {"task": task_after_edit})
        else:
            task_after_edit["message"] = (
                "Please ensure that description of your task is longer then 1 symbol and shorter then 1000"
            )
            task_after_edit["task"] = task.dict_with_convert_time_field_to_json()
            return render(request, "task_edit.html", task_after_edit)

    elif request.method == "DELETE":
        task_dict = delete_task(task)
        return render(
            request,
            "notify_form.html",
            {
                "message": f"Task with description: \n {task.description} \n was deleted",
                "task": task_dict,
            },
        )


@decorators.login_required
@csrf_exempt
def get_edit_form(request, task_id):
    if request.method == "GET":
        task = models.Task.objects.get(id=task_id)
        task = get_task(task)
        return render(request, "task_edit.html", {"task": task})
