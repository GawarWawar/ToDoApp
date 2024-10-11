from django.contrib import admin
from schedule import models

class ProjectAdmin(admin.ModelAdmin):
    ...
    
class TaskAdmin(admin.ModelAdmin):
    ...

# Register your models here.
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)