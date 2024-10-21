from django.db import models
import datetime
from django_instance import settings
from .src import models_methods


# Create your models here.
class Project(models.Model, models_methods.ModelsWithTimeFIelds):
    user_instance = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name="Name", max_length=100)
    creation_date = models.DateTimeField(
        verbose_name="Date of Creation", default=datetime.datetime.now
    )
    expire_date = models.DateTimeField(
        verbose_name="Date of expiration", blank=True, null=True, default=None
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_instance": {
                "id": self.user_instance.id,
            },
            "name": self.name,
            "creation_date": self.creation_date,
            "expire_date": self.expire_date,
        }
        
    def to_dict_with_tasks(self, only_task_id = False) -> dict[str]:
        self_dict = self.dict_with_convert_time_field_to_json()
        
        self_dict["tasks"] = []
        for task in Task.objects.filter(project_instance=self):
            if only_task_id:
                self_dict["tasks"].append(task.id)
            else:
                self_dict["tasks"].append(
                    task.dict_with_convert_time_field_to_json()
                )

        return self_dict

    def __str__(self):
        return self.name


class Task(models.Model, models_methods.ModelsWithTimeFIelds):
    project_instance = models.ForeignKey(
        Project, verbose_name="Project", on_delete=models.CASCADE
    )
    description = models.CharField(verbose_name="Description", max_length=1000)
    priority = models.IntegerField(verbose_name="Priority")
    creation_date = models.DateTimeField(
        verbose_name="Date of Creation", default=datetime.datetime.now
    )
    expire_date = models.DateTimeField(
        verbose_name="Date of expiration", blank=True, null=True, default=None
    )
    is_completed = models.BooleanField(verbose_name="Complition status", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "project_instance": {
                "id": self.project_instance.id,
            },
            "description": self.description,
            "creation_date": self.creation_date,
            "expire_date": self.expire_date,
            "is_completed": self.is_completed,
        }

    def __str__(self):
        return self.description
