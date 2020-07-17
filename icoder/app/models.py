from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    usn=models.CharField(max_length=30,primary_key=True)
    year=models.IntegerField()
    branch=models.CharField(max_length=10)
    cname=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    