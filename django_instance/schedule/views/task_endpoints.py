from allauth.account import decorators

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.task_actions import get_task, edit_task, delete_task 


@decorators.login_required
@csrf_exempt
def project_task_endpoint(request, project_id, task_id):
    try:
        project = models.Project.objects.get(id = project_id)
        task = models.Task.objects.get(id = task_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status = 404)
    
    if request.method == "GET":
        return HttpResponse(get_task(task))
    elif request.method == "POST":     
        return HttpResponse(edit_task(task, task_info))
    elif request.method == "DELETE":
        return HttpResponse(delete_task(task))