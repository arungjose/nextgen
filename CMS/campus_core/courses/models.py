from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=30)
    spec=models.CharField(max_length=60)
    fee=models.IntegerField()
    accr=models.BooleanField()
