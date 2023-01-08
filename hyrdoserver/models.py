from django.db import models

# Create your models here.

class members(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    
class ocupation(models.Model):
    jobtype = models.CharField(max_length=250)
    
class person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    jobtype = models.CharField(max_length=250)
    

