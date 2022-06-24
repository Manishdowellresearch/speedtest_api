from django.db import models

# Create your models here.

class Speed_test_data(models.Model):
    download_speed = models.CharField(max_length=30, blank=True)
    upload_speed = models.CharField(max_length=30, blank=True)

