from django.db import models

# Create your models here.
class Event(models.Model):
    type = models.CharField(max_length = 50, null = False)
    datetime = models.DateTimeField()
    description = models.CharField(max_length = 200, null = False)
    baby = models.ForeignKey(
        'baby.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = False
    )

    def __str__(self):
        return 'Event: {0} (baby:{1}, date:{2})'.format(self.type, self.baby, self.datetime)