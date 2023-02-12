from django.db import models
import uuid
# Create your models here.
from users.models import Profile
from ckeditor.fields import RichTextField 


class Project(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
 
    body = RichTextField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, default="None", upload_to="images/profiles")
   
    vote_total = models.IntegerField(null=True, blank=True, default=0)
    vote_ratio = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = '/images/caveman.jpeg'
        return url


