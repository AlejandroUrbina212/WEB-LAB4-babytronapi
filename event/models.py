from django.utils.timezone import now
from django.db import models


class Event(models.Model):
    type = models.CharField(max_length = 50, null = False)
    datetime = models.DateTimeField(default = now)
    description = models.CharField(max_length = 100, null = False)
    baby = models.ForeignKey(
        'baby.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = False
    )

    def __str__(self):
        return 'Event: {0} / Baby:{1}/  EventDate:{2}'.format(self.type, self.baby, self.datetime)