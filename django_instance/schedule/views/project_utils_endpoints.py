from allauth.account import decorators
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@decorators.login_required
@csrf_exempt
def get_add_form(request):
    return render(request, "add_project_form.html")


@decorators.login_required
@csrf_exempt
def get_add_button(request):
    return render(request, "add_project_button.html")
