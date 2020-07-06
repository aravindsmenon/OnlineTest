from django.db import models
from datetime import date
# Create your models here.
class files(models.Model):
    filename=models.CharField(max_length=200)
    path=models.CharField(max_length=500)
    filesize=models.CharField(max_length=200)
    extension=models.CharField(max_length=200)

    def __str__(self):
        return self.filename