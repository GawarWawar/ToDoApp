from django.urls import path

from schedule.views.project_endpoints import project_endpoint
from schedule.views.projects_endpoints import projects_endpoint
from schedule.views.task_endpoints import task_endpoint
from schedule.views.tasks_endpoints import project_tasks_endpoint


urlpatterns = [
    path("projects/", projects_endpoint, name="projects"),
    path('projects/create', projects_endpoint, name="new_project"),
    
    path('projects/<project_id>', project_endpoint, name="project_details"),
    path('projects/<project_id>/edit', project_endpoint, name="edit_project"),
    path('projects/<project_id>/delete', project_endpoint, name="delete_project"),
    
    path("projects/<project_id>/tasks/", project_tasks_endpoint, name="project_tasks"), #depricated(included in project_details)
    path("projects/<project_id>/tasks/create", project_tasks_endpoint, name="create_task_for_project"),
    
    path("tasks/<task_id>", task_endpoint, name="task_details"),
    path("tasks/<task_id>/edit", task_endpoint, name="edit_task"),
    path("tasks/<task_id>/delete", task_endpoint, name="delete_task"),
    

]
