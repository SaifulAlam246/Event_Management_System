from django.db import models
from django.utils import timezone
from datetime import date
from django.conf import settings


def current_time():
    return timezone.now().time()

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=date.today)  
    time = models.TimeField(default=current_time, null=True, blank=True) 
    location = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    event_image = models.ImageField(upload_to='events_image',  blank=True, null=True,
                              default="events_image/defout_img.png")
    participants=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='events')


    def __str__(self):
        return self.name
    


