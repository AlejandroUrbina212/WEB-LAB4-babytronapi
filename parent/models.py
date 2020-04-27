from django.db import models

# Create your models here.
class Parent(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname
