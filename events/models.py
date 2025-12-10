from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=200),
    description=models.TextField(),
    date=models.DateField(),
    time=models.TimeField(),
    location=models.CharField(max_length=300)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

class Participant(models.Model):
    name=models.CharField(max_length=200),
    email=models.EmailField(unique=True),
    event=models.ManyToManyField(Event,related_name='participants')

class Category(models.Model):
    name=models.CharField(max_length=200),
    description=models.TextField()