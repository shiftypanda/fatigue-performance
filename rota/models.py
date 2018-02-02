from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class ShiftPattern(models.Model):
    shift_name = models.CharField(max_length=40)
    start_time = models.TimeField()
    finish_time = models.TimeField()

    def __str__(self):
        return self.shift_name


class RotaShift(ShiftPattern):
    rota_name = models.ForeignKey(ShiftPattern, on_delete=models.CASCADE, related_name='+')
    rota_start_time = ShiftPattern.start_time
    rota_finish_time = ShiftPattern.finish_time

    def __str__(self):
        return self.rota_name

class ActualShift(RotaShift):
    actual_shift_name = models.ForeignKey(RotaShift, on_delete=models.CASCADE, related_name='+')
    actual_start_time = RotaShift.rota_start_time
    actual_finish_time = RotaShift.rota_finish_time

    def __str__(self):
        return self.actual_shift_name
