from django.urls import path, include
from . import views

urlpatterns = [
    path("projects/<project_id>/tasks/create", views.task)
]