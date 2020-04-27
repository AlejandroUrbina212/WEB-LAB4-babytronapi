from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Parent(models.Model):
    username = models.CharField(max_length = 100, default = "admin")
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname
