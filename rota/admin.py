from django.contrib import admin

# Register your models here.
from .models import ShiftPattern, RotaShift, ActualShift

admin.site.register(ShiftPattern)
admin.site.register(RotaShift)
admin.site.register(ActualShift)
