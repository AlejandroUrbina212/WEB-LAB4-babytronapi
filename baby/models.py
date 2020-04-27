from django.db import models

# Create your models here.


class Baby(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(
        'parent.Parent',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.firstname + " " + self.lastname