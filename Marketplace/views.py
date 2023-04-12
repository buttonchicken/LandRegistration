from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Accounts.models import User
from .models import *
from .serializers import * 

class Insert_Property(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        try:
            mark_obj = Marketplace.objects.create(
                owner = request.user,
                name = data['name'],
                price = data['price'],
                token_id = data['token_id'],
                image = data['image_file']
            )
            serialized_obj = MarketplaceSerializer(mark_obj)
            return Response({'success':True,'message':'Property listed successfully','payload':serialized_obj.data},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response({'success':False,'message':'Please enter all the data'},status=status.HTTP_400_BAD_REQUEST)

class ViewMarketplace(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            maketplace_objs = Marketplace.objects.all()
            serialized_objs = MarketplaceSerializer(maketplace_objs, many=True)
            serialized_data = serialized_objs.data
            return Response({'success':True,'Marketplace':serialized_data},status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'success':False,'message':'No listings found'},status=status.HTTP_400_BAD_REQUEST)