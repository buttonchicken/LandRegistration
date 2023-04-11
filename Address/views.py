from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Accounts.models import User
from .models import *
from .serializers import *
# Create your views here.
#POST api - insert address
#GET api - by admin

class Insert_Address(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        try:
            admin_obj = User.objects.get(UUID=data['admin_UUID'])
            user_obj = User.objects.get(UUID=data['owner_UUID'])
            addr_obj = Address.objects.create(admin_incharge=admin_obj,owned_by=user_obj,
                                              token_id=data['token_id'],area_code=data['area_code'],
                                              city=data['city'],state=data['state'],category=data['category'],
                                              district=data['district'],sub_registrar_office=data['sub_registrar_office'],
                                              village=data['village'],ward_no=data['ward_no'],
                                              total_extend=data['total_extend'],extend_of_land=data['extend_of_land'],
                                              street_name=data['street_name'],door_no=data['door_no'],house_no=data['house_no'],
                                              dimension=data['dimension'],metadata=data['metadata'],in_marketplace=data['in_marketplace'])
            serializer = AddressSerializer(addr_obj)
            return Response({"success":True,"message":"Inserted address successfully","data":serializer.data},status=status.HTTP_200_OK)
        except:
            return Response({"success":False,"message":"Error"},status=status.HTTP_200_OK)
