from allauth.account import decorators
from django.shortcuts import render

from django_instance.settings import JS_TIME_FORMAT


@decorators.login_required
def index(request):
    return render(request, "index.html")