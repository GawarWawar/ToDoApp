import json
from django.shortcuts import render, HttpResponse
from allauth.account import decorators
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.
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
def project_endpoint(request):
    if request.method == "GET":
        projects = models.Project.objects.filter(user_instance = request.user)
        all_projects = []
        for project in projects:
            proj_dict = project.convert_time_field_to_json()
            all_projects.append(proj_dict)
        context = json.dumps(all_projects)
        print(context)
    
    elif request.method == "POST":

        # new_project = models.Project.objects.create(
        #     user_instance = request.user,
        #     name = request.project["name"]
        # )
        
        greating_string = f"Hi"
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
        project_instance = models.Project.objects.get(id = project_id)
        task_description = request.POST["description"]
        if task_description is not "" and len(task_description) < 1000:
            new_task = models.Task.objects.create(
                project_instance = project_instance,
                description = task_description,
                priority = 0,
            )
            new_task.save()
            context = new_task.convert_time_field_to_json()
        else:
            context = {"error": "Bad description"}
    return HttpResponse(context)

