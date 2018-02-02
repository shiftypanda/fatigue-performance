from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    greeting_text = models.CharField(max_length=80)

    def __str__(self):
        return self.greeting_text

class ReadyCheck(models.Model):
    name = models.CharField(max_length=30)
    test_length = models.IntegerField(default=5)



    def __str__(self):
        return self.name
