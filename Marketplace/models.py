from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

def upload_to(instance,filename):
    return '{0}/{1}/{2}'.format(instance.owner.Aadhaar_no, instance.name,filename)

class Marketplace(models.Model):
    owner = models.ForeignKey("Accounts.User", on_delete=models.CASCADE, blank=True, null=True,related_name="owner")
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    token_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return str(self.owner.username) + "-" +str(self.name)