from django.db import models
from django.utils import timezone

import datetime

current_date = timezone.now

# Create your models here.
class Shift(models.Model):
    start_time = models.DateTimeField(default=current_date)
    finish_time = models.DateTimeField(blank=True, null=True)

    @property
    def shift_length(self):
        return self.finish_time - self.start_time
