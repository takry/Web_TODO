from django.db import models

from authapp.models import Project, UserAuth


# Create your models here.

class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    add_datetime = models.DateTimeField(auto_now_add=True)
    update_datatime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
