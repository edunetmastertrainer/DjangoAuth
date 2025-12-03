from django.db import models
from django.db.models import Model
# Create your models here.
class Profile(models.Model):
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.email