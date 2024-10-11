from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    creation_date = models.DateTimeField(verbose_name="Date of Creation", default=datetime.datetime.now)
    expire_date = models.DateTimeField(verbose_name="Date of expiration", null=True, default=None)

class Task(models.Model):
    project_instance = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Description", max_length=1000)
    priority = models.IntegerField(verbose_name="Priority")
    creation_date = models.DateTimeField(verbose_name="Date of Creation", default=datetime.datetime.now)
    expire_date = models.DateTimeField(verbose_name="Date of expiration", null=True, default=None)
