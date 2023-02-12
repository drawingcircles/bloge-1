from django.db import models
from .models import *
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, max_length=20, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(default="{% static 'images/spongebob-patrick.gif'%}", blank=True, null=True, upload_to="profiles/")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['-created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/caveman.jpeg'

        return url 


