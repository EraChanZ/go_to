from django.db import models
from django.utils import timezone
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    def __str__ (self):
        return self.first_name

class Dann(models.Model):
    #title = models.CharField(max_length=250)
    kek = models.TextField()
    #idd_x = models.TextField()
    #created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    #due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__ (self):
        return self.kek