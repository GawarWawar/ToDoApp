from django.urls import path, include
from . import views

urlpatterns = [
    path("projects/", views.projects_endpoint),
    path('projects/create', views.projects_endpoint),
    
    path('projects/<project_id>/edit', views.project_endpoint),
    path('projects/<project_id>/delete', views.project_endpoint),
    
    path("projects/<project_id>/tasks/", views.project_tasks_endpoint),
    path("projects/<project_id>/tasks/create", views.project_tasks_endpoint),
    
    path("projects/<project_id>/tasks/<task_id>/edit", views.project_task_endpoint),
    path("projects/<project_id>/tasks/<task_id>/delete", views.project_task_endpoint),

]