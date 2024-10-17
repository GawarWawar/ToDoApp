from allauth.account import decorators

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.task_actions import get_all_tasks, create_new_task

@decorators.login_required
@csrf_exempt
def project_tasks_endpoint(request, project_id):
    try:
        project = models.Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status = 404)
    
    if request.method == "GET":
        return HttpResponse(get_all_tasks(project))
    if request.method == "POST":
        return HttpResponse(create_new_task(request.POST, project))
    