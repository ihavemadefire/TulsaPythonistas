from django.db import models
from django.db.models.enums import TextChoices
from djrichtextfield.models import RichTextField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = RichTextField()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    when = models.DateTimeField()
    date = models.DateField()
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    description = models.TextField()


    def __str__(self):
        return self.title