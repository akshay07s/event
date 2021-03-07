from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Places(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=50)
    data=models.CharField(max_length=500)
    time=models.DateTimeField(blank=True)
    location=models.CharField(max_length=50)
    image=models.ImageField(upload_to='event_images')
    like_by=models.ManyToManyField(User,blank=True)
    like=models.BooleanField(default=False)

    def __str__(self):
        return self.event_name