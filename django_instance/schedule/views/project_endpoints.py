from allauth.account import decorators

from django.http import QueryDict
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.project_actions import get_project, edit_project, delete_project

@decorators.login_required
@csrf_exempt
def project_endpoint(request, project_id):
    try:
        project = models.Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)

    if request.method == "GET":
        return render(request, "project_id.html", {"project": get_project(project)})

    elif request.method == "PUT":
        project_info = QueryDict(request.body)

        project_after_edit = edit_project(project, project_info)
        return render(request, "project_header.html", {"project": project_after_edit})

    elif request.method == "DELETE":
        project_dict = delete_project(project)
        
        return render(
            request, "notify_form.html", 
            {
                "message": f"TODO list with name: \n {project.name} \n was deleted",
                "project": project_dict
            }
        ) 

@decorators.login_required
@csrf_exempt
def get_edit_form(request, project_id):
    if request.method == "GET":
        project = models.Project.objects.get(id=project_id)
        project = get_project(project)
        return render(request, "project_edit.html", {"project": project})
    
@decorators.login_required
@csrf_exempt
def sort_project (request, project_id):
    if request.method == "POST":
        project = models.Project.objects.get(id=project_id)    
        task_list = request.POST.getlist("priority_by_id")
        task_list_end = len(task_list)-1
        for priority, task_id in enumerate(task_list):
            task = models.Task.objects.get(id=task_id)
            task.priority = task_list_end-priority
            task.save()
        
    return render(request, "project_id.html", {"project": project.to_dict_with_tasks()})

@decorators.login_required
@csrf_exempt 
def get_project_header(request, project_id):
    project = models.Project.objects.get(id=project_id)
    project_dict = get_project(project)
    project_dict.pop("tasks")
    return render(request, "project_header.html", {"project": project_dict})