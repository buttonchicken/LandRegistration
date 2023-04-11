from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    Aadhaar_no = models.CharField(max_length=12,unique=True,null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    mobile_number = models.CharField(max_length=10,null=True,blank=True)
    UUID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

class Otp(models.Model):
    value = models.CharField(max_length=4)
    email_id = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    valid_upto = models.DateTimeField(blank=True)
    
    def save(self, *args, **kwargs):
        self.valid_upto = self.created_at + timedelta(minutes=1)
        super(Otp, self).save(*args, **kwargs)