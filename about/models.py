import json

from django.db import models
from django.utils.timezone import now
# Create your models here.

class ImageModel(models.Model):
    club = models.CharField(max_length=10)
    image = models.FileField(null=True, upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.IntegerField()
