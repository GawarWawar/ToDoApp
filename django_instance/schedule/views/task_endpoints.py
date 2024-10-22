from allauth.account import decorators

from django.http import QueryDict
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.task_actions import get_task, edit_task, delete_task

@decorators.login_required
@csrf_exempt
def task_endpoint(request, task_id):
    if request.method == "GET":
        try:
            task = models.Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)
        task_details = {"task": get_task(task)}
        return render(request, "task_id.html", context=task_details)
    
    elif request.method == "PUT":
        try:
            task = models.Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)

        task_info = QueryDict(request.body)

        task_after_edit = edit_task(task, task_info)
        return render(request, "task_id.html", {"task": task_after_edit})
    
    elif request.method == "DELETE":
        try:
            task = models.Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return render(
                request, "task_change_confirm.html", 
                {
                    "error": "Bad ID", 
                    "message": "Could not delete task with this id"
                }
            )
        
        task_dict = delete_task(task)
        return render(
            request, "task_change_confirm.html", 
            {
                "message": f"Task with description: \n {task.description} \n was deleted",
                "task": task_dict
            }
        )
 

@decorators.login_required
@csrf_exempt       
def get_edit_form(request, task_id):
    if request.method == "GET":
        task = models.Task.objects.get(id=task_id)
        task = get_task(task)
        return render(request, "task_edit.html", {"task": task})