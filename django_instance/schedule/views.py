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
        proj_dict = project.convert_time_field_to_json()
        proj_dict["tasks"] = []
        for task in tasks:
            task_dict = task.convert_time_field_to_json()
            proj_dict["tasks"].append(task_dict)
        all_tasks.append(proj_dict)
    task_collection_json = json.dumps(all_tasks)
    return render(request, "index.html", {"data": task_collection_json})