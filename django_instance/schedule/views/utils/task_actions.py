import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import json

from django_instance.settings import JS_TIME_FORMAT
from schedule import models

def get_all_tasks(project_id:int):
    try:
        project_instance = models.Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status = 404)
    
    tasks = models.Task.objects.filter(project_instance = project_instance)
    all_tasks = []
    for task in tasks:
        proj_dict = task.dict_with_convert_time_field_to_json()
        all_tasks.append(proj_dict)
    return HttpResponse(json.dumps(all_tasks))

def create_new_task(task_info:dict, project_id:int):
    try:
        task_description = task_info["description"]
    except MultiValueDictKeyError:
        return HttpResponse(json.dumps({"error": "Bad POST"}), status = 422)
        
    try:
        project_instance = models.Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        context = json.dumps({"error": "Bad ID"})
        status=404
        return HttpResponse(context, status = status)
    
    
    if task_description != "" and len(task_description) < 1000:
        new_task = models.Task.objects.create(
            project_instance = project_instance,
            description = task_description,
            priority = 0,
        )
        new_task.save()
        return HttpResponse(new_task.dict_with_convert_time_field_to_json())
    else:
        return HttpResponse(json.dumps({"error": "Bad POST"}), status=422)
    
def get_task(task:models.Task):
    HttpResponse(json.dumps(task.dict_with_convert_time_field_to_json()))
        
def edit_task(task:models.Task, task_info: dict):
    try:
        description = task_info["description"]
        expire_date = task_info["expire_date"]
    except MultiValueDictKeyError:
        context = json.dumps({"error": "Bad POST"})
        status=422
        return HttpResponse(context, status = status)

    if 0 < len(description) < 1000: 
        task.description = description
    else:
        return HttpResponse(json.dumps({"error": "Bad POST"}), status=422)
    
    if expire_date == "" :
        expire_date = None
    else:
        expire_date = datetime.datetime.strptime(expire_date, JS_TIME_FORMAT)
    task.expire_date = expire_date
    
    task.save()
    return HttpResponse(task.dict_with_convert_time_field_to_json())

def delete_task(task:models.Task):
    respnse = HttpResponse(json.dumps(task.dict_with_convert_time_field_to_json()))
    task.delete()
    return respnse