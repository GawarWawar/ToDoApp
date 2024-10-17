from allauth.account import decorators
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

import json

from django_instance.settings import JS_TIME_FORMAT
from schedule import models

decorators.login_required
@csrf_exempt
def projects_endpoint(request):
    if request.method == "GET":
        projects = models.Project.objects.filter(user_instance = request.user)
        all_projects = []
        for project in projects:
            proj_dict = project.dict_with_convert_time_field_to_json()
            all_projects.append(proj_dict)
        context = json.dumps(all_projects)
    
    elif request.method == "POST":
        try:
            name = request.POST["name"]
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
        context = new_project.dict_with_convert_time_field_to_json()
        
    return HttpResponse(context)
        
decorators.login_required
@csrf_exempt
def project_endpoint(request, project_id):
    if request.method == "GET":
        try:
            project = models.Project.objects.get(id = project_id)
        except ObjectDoesNotExist:
            context = json.dumps({"error": "Bad ID"})
            status=404
            return HttpResponse(context, status = status)
        context = json.dumps(project.dict_with_convert_time_field_to_json())
    elif request.method == "POST":
        try:
            name = request.POST["name"]
            expire_date = request.POST["expire_date"]
        except MultiValueDictKeyError:
            context = json.dumps({"error": "Bad POST"})
            status=422
            return HttpResponse(context, status = status)

        try:
            project = models.Project.objects.get(id = project_id)
        except ObjectDoesNotExist:
            context = json.dumps({"error": "Bad ID"})
            status=404
            return HttpResponse(context, status = status)

        if 0 < len(name) <= 100: 
            project.name = name
        else:
            context = json.dumps({"error": "Bad POST"})
            status = 422
            return HttpResponse(context, status=status)
        
        if expire_date == "" :
            expire_date = None
        else:
            expire_date = datetime.datetime.strptime(expire_date, JS_TIME_FORMAT)
        project.expire_date = expire_date
        
        project.save()
        
        context = project.dict_with_convert_time_field_to_json()
        
    elif request.method == "DELETE":
        try:
            project_to_delete = models.Project.objects.get(pk = project_id)
        except ObjectDoesNotExist:
            context = json.dumps({"error": "Bad ID"})
            status=404
            return HttpResponse(context, status = status)
        project_to_delete.delete()
        context = json.dumps(project_to_delete.dict_with_convert_time_field_to_json())
        
    return HttpResponse(context)