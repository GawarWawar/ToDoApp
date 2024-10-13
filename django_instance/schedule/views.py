import json
from django.shortcuts import render, HttpResponse
from allauth.account import decorators
from . import models
# Create your views here.
@decorators.login_required
def get_users_projects(request):
    TIME_FORMAT = "%d/%m/%Y, %H:%M:%S"
    
    projects = models.Project.objects.filter(user_instance = request.user)
    # list_of_projects = [project.name for project in projects]
    all_tasks = []
    for project in projects:
        tasks = models.Task.objects.filter(project_instance = project)
        proj_dict = {
            "name": project.name, 
            "creation_date": project.creation_date.strftime(TIME_FORMAT),
            "expire_date": 
                project.expire_date if project.expire_date is None 
                    else project.expire_date.strftime(TIME_FORMAT),
            "tasks": []
        }
        for task in tasks:
            task_dict = {
                "description": task.description,
                "priority": task.priority,
                "creation_date": task.creation_date.strftime(TIME_FORMAT),
                "expire_date": 
                    task.expire_date if task.expire_date is None 
                        else task.expire_date.strftime(TIME_FORMAT),
            }
            proj_dict["tasks"].append(task_dict)
        all_tasks.append(proj_dict)
    task_collection_json = json.dumps(all_tasks)
    return render(request, "index.html", {"data": task_collection_json})