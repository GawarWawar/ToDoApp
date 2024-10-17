from allauth.account import decorators
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

import json

from django_instance.settings import JS_TIME_FORMAT
from . import models

# Create your views here.
@decorators.login_required
def get_users_projects(request):    
    projects = models.Project.objects.filter(user_instance = request.user)
    all_tasks = []
    for project in projects:
        tasks = models.Task.objects.filter(project_instance = project)
        proj_dict = project.dict_with_convert_time_field_to_json()
        proj_dict["tasks"] = []
        for task in tasks:
            task_dict = task.dict_with_convert_time_field_to_json()
            proj_dict["tasks"].append(task_dict)
        all_tasks.append(proj_dict)
    task_collection_json = json.dumps(all_tasks)
    return render(request, "index.html", {"data": task_collection_json})

