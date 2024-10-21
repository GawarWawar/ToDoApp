from allauth.account import decorators

from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.task_actions import get_all_tasks, create_new_task


@decorators.login_required
@csrf_exempt
def project_tasks_endpoint(request, project_id):
    try:
        project = models.Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)

    if request.method == "GET":
        tasks = get_all_tasks(project)
        
        return render(request, "project_tasks.html", tasks)
    if request.method == "POST":
        status = None
        task, status = create_new_task(request.POST, project)
        
        return render(request, "task_id.html", task, status=status)
