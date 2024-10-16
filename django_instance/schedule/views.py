import datetime
from django.shortcuts import render, HttpResponse
from allauth.account import decorators
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

import json
from . import models
from django_instance.settings import JS_TIME_FORMAT
# Create your views here.
@decorators.login_required
def index(request):
    return render(request, "index.html")

@decorators.login_required
def get_users_projects(request):    
    projects = models.Project.objects.filter(user_instance = request.user)
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

decorators.login_required
@csrf_exempt
def project_endpoint(request):
    if request.method == "GET":
        projects = models.Project.objects.filter(user_instance = request.user)
        all_projects = []
        for project in projects:
            proj_dict = project.convert_time_field_to_json()
            all_projects.append(proj_dict)
        context = json.dumps(all_projects)
    
    elif request.method == "POST":
        try:
            expire_date = request.POST["expire_date"]
        except MultiValueDictKeyError:
            context = json.dumps({"error": "Bad POST"})
            status=422
            return HttpResponse(context, status = status)
        
        if name == "":
            name = "PlaceHolder"  
            
        if expire_date == "" :
            expire_date = None
        else:
            expire_date = datetime.datetime.strptime(expire_date, JS_TIME_FORMAT)

        new_project = models.Project.objects.create(
            user_instance = request.user,
            name = name,
            expire_date = expire_date
        )
        new_project.save()
        context = new_project.convert_time_field_to_json()
        
    return HttpResponse(context)
        

@decorators.login_required
@csrf_exempt
def task_endpoint(request, project_id):
    if request.method == "GET":
        project_instance = models.Project.objects.get(id = project_id)
        
        tasks = models.Task.objects.filter(project_instance = project_instance)
        all_tasks = []
        for task in tasks:
            proj_dict = task.convert_time_field_to_json()
            all_tasks.append(proj_dict)
        context = json.dumps(all_tasks)
    if request.method == "POST":
        try:
            task_description = request.POST["description"]
        except MultiValueDictKeyError:
            context = json.dumps({"error": "Bad POST"})
            status=422
            return HttpResponse(context, status = status)
            
        project_instance = models.Project.objects.get(id = project_id)
        if task_description is not "" and len(task_description) < 1000:
            new_task = models.Task.objects.create(
                project_instance = project_instance,
                description = task_description,
                priority = 0,
            )
            new_task.save()
            context = new_task.convert_time_field_to_json()
        else:
            context = json.dumps({"error": "Bad POST"})
            status = 422
            return HttpResponse(context, status=status)
            context = {"error": "Bad description"}
    return HttpResponse(context)

