from allauth.account import decorators

from django.shortcuts import HttpResponse
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
        return HttpResponse(get_project(project))

    elif request.method == "POST":
        return HttpResponse(edit_project(project, request.POST))

    elif request.method == "DELETE":
        return HttpResponse(delete_project(project))
