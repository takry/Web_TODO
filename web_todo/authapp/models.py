from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserAuth(AbstractUser):
    email = models.EmailField(unique=True)


class Project(models.Model):
    name = models.CharField(max_length=64)
    url_repo = models.URLField(max_length=64, null=True)
    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE)

