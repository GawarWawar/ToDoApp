from allauth.account import decorators

from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.task_actions import get_task, edit_task, delete_task


@decorators.login_required
@csrf_exempt
def project_task_endpoint(request, project_id, task_id):
    try:
        models.Project.objects.get(id=project_id)
        task = models.Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)

    if request.method == "GET":
        return HttpResponse(get_task(task))
    elif request.method == "POST":
        try:
            task_info = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            task_info = request.POST

        return HttpResponse(edit_task(task, task_info))
    elif request.method == "DELETE":
        return HttpResponse(delete_task(task))

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
    
    elif request.method == "POST":
        try:
            task = models.Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)
        try:
            task_info = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            task_info = request.POST

        return HttpResponse(edit_task(task, task_info))
    elif request.method == "DELETE":
        try:
            task = models.Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)
        return HttpResponse(delete_task(task))