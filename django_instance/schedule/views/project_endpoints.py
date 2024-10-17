from allauth.account import decorators

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.project_actions import get_project, edit_project, delete_project 

decorators.login_required
@csrf_exempt
def project_endpoint(request, project_id):
    if request.method == "GET":
        response = get_project(project_id)
            
    elif request.method == "POST":
        response = edit_project(project_id, request.POST)
        
    elif request.method == "DELETE":
        response = delete_project(project_id)
        
    return HttpResponse(response)