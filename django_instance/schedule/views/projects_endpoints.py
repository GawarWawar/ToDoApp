from allauth.account import decorators
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.project_actions import get_all_projects, create_new_project

decorators.login_required


@csrf_exempt
def projects_endpoint(request):
    if request.method == "GET":
        return HttpResponse(get_all_projects(request.user))

    elif request.method == "POST":
        return HttpResponse(create_new_project(request.POST, request.user))
