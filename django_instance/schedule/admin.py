from django.contrib import admin
from schedule import models

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "user_instance", "creation_date", "expire_date"]
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "project_instance", "description", "priority", "creation_date", "expire_date", "is_completed"]

# Register your models here.
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)