from allauth.account import decorators
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.task_actions import get_all_tasks, create_new_task

@decorators.login_required
@csrf_exempt
def project_tasks_endpoint(request, project_id):
    if request.method == "GET":
        response = get_all_tasks(project_id)
    if request.method == "POST":
        response = create_new_task(request.POST, project_id)
    return HttpResponse(response)
    