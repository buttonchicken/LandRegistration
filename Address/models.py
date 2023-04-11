from django.db import models
from django.utils import timezone

class Address(models.Model):
    admin_incharge = models.ForeignKey("Accounts.User", on_delete=models.CASCADE, blank=True, null=True, related_name="admincharge")
    owned_by = models.ForeignKey("Accounts.User", on_delete=models.CASCADE, blank=True, null=True,related_name="ownedby")
    token_id = models.CharField(max_length=100)
    area_code = models.CharField(max_length=256,blank = True)
    city = models.CharField(max_length=256,blank = True)
    state = models.CharField(max_length=256,blank = True)
    category = models.CharField(max_length=256,blank = True)
    district = models.CharField(max_length=256,blank = True)
    sub_registrar_office = models.CharField(max_length=256,blank = True)
    village = models.CharField(max_length=256,blank = True)
    ward_no = models.CharField(max_length=256,blank = True)
    total_extend = models.CharField(max_length=256,blank = True)
    extend_of_land = models.CharField(max_length=256,blank = True)
    street_name = models.CharField(max_length=256,blank = True)
    door_no = models.CharField(max_length=256,blank = True)
    house_no = models.CharField(max_length=256,blank = True)
    dimension = models.CharField(max_length=256,blank = True)
    metadata = models.CharField(max_length=256,blank = True)
    in_marketplace = models.BooleanField(default=False)
