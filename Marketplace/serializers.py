from .models import *
from rest_framework import serializers

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = ['owner','id','name','price','token_id','created_at','image']