from allauth.account import decorators
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from .utils.project_actions import get_all_projects, create_new_project

@decorators.login_required
@csrf_exempt
def projects_endpoint(request):
    if request.method == "GET":
        projects = get_all_projects(request.user)
        return render(request, "get_all_projects.html", projects)

    elif request.method == "POST":
        new_project = create_new_project(request.POST, request.user)
        return render(request, "project_id.html", {"project": new_project})
