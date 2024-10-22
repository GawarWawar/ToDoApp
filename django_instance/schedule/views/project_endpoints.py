from allauth.account import decorators

from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json

from schedule import models
from .utils.project_actions import get_project, edit_project, delete_project

decorators.login_required


@csrf_exempt
def project_endpoint(request, project_id):
    try:
        project = models.Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Bad ID"}), status=404)

    if request.method == "GET":
        return render(request, "project_id.html", {"project": get_project(project)})

    elif request.method == "POST":
        return HttpResponse(edit_project(project, request.POST))

    elif request.method == "DELETE":
        project_dict = delete_project(project)
        
        return render(
            request, "after_delete_form.html", 
            {
                "message": f"TODO list with name: \n {project.name} \n was deleted",
                "project": project_dict
            }
        ) 
