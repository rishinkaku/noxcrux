from django.db import models
from django.contrib.auth.models import User


class Horcrux(models.Model):
    site = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    horcrux = models.CharField(max_length=255)

    def __str__(self):
        return self.name
