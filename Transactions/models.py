from django.db import models
from .constants import TRANSACTION_STATUS
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    sender = models.ForeignKey("Accounts.User", on_delete=models.CASCADE, blank=True, null=True, related_name="sender")
    reciever = models.ForeignKey("Accounts.User", on_delete=models.CASCADE, blank=True, null=True, related_name="reciever")
    transaction_id = models.CharField(max_length=256)
    status = models.CharField(max_length = 20,choices = TRANSACTION_STATUS,default = 'INITIATED')
    created_at = models.DateTimeField(default=timezone.now, editable=False)