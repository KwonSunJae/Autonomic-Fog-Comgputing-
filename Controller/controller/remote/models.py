from django.db import models

# Create your models here.

class Remote(models.Model):
    type = models.IntegerField()
    