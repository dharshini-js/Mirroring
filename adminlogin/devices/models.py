from django.db import models

# Create your models here.
class device(models.Model):
    device_name=models.CharField(max_length=100)
    device_type=models.CharField(max_length=30)
    device_model=models.CharField(max_length=300)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

