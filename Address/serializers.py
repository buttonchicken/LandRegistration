from .models import *
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['token_id','area_code','city','state','category','district',
                  'sub_registrar_office','village','ward_no','total_extend',
                  'extend_of_land','street_name','door_no','house_no','dimension',
                  'metadata']