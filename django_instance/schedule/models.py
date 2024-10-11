from django.db import models
import datetime
from django_instance import settings

# Create your models here.
class Project(models.Model):
    user_instance = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=100)
    creation_date = models.DateTimeField(verbose_name="Date of Creation", default=datetime.datetime.now)
    expire_date = models.DateTimeField(verbose_name="Date of expiration", blank=True, null=True, default=None)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    project_instance = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Description", max_length=1000)
    priority = models.IntegerField(verbose_name="Priority")
    creation_date = models.DateTimeField(verbose_name="Date of Creation", default=datetime.datetime.now)
    expire_date = models.DateTimeField(verbose_name="Date of expiration", blank=True, null=True, default=None)
