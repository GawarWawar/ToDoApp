from django.urls import path, include
from . import views

urlpatterns = [
    path("projects/", views.project_endpoint),
    path("projects/<project_id>/tasks/", views.task_endpoint),
    path("projects/<project_id>/tasks/create", views.task_endpoint)
]