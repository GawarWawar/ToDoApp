# Generated by Django 5.1.2 on 2024-10-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False, verbose_name="Complition status"),
        ),
    ]
