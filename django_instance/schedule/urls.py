from django.urls import path

from schedule.views.project_endpoints import project_endpoint
from schedule.views.projects_endpoints import projects_endpoint
from schedule.views.task_endpoints import project_task_endpoint
from schedule.views.tasks_endpoints import project_tasks_endpoint


urlpatterns = [
    path("projects/", projects_endpoint),
    path('projects/create', projects_endpoint),
    
    path('projects/<project_id>/edit', project_endpoint),
    path('projects/<project_id>/delete', project_endpoint),
    
    path("projects/<project_id>/tasks/", project_tasks_endpoint),
    path("projects/<project_id>/tasks/create", project_tasks_endpoint),
    
    path("projects/<project_id>/tasks/<task_id>/edit", project_task_endpoint),
    path("projects/<project_id>/tasks/<task_id>/delete", project_task_endpoint),

]
