from django.db import models



class fibonacci(models.Model):
    number = models.CharField(max_length=100)
    time = models.CharField(max_length=300, null=True)

# Create your models here.
