from allauth.account import decorators
from django.shortcuts import render


@decorators.login_required
def index(request):
    return render(request, "index.html")
