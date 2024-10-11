from django.contrib import admin
from schedule import models

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["user_instance", "name", "creation_date", "expire_date"]
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ["project_instance", "description", "priority", "creation_date", "expire_date"]

# Register your models here.
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)