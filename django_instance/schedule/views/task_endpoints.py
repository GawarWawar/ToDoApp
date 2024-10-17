from allauth.account import decorators
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.task_actions import get_task, edit_task, delete_task 


@decorators.login_required
@csrf_exempt
def project_task_endpoint(request, project_id, task_id):
    if request.method == "GET":
        response = get_task(task_id)
    elif request.method == "POST":        
        response = edit_task(task_id, request.POST)
    elif request.method == "DELETE":
        response = delete_task(task_id)

    return HttpResponse(response)