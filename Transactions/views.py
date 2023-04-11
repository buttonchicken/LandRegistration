#GET TRANSACTION- by t_id, by user
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Accounts.models import User
from .models import *
from .serializers import *

class Capture_Transaction(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        try:
            sender_obj = request.user
            reciever_obj = User.objects.get(UUID = data['reciever_uuid'])
            trans_obj = Transaction.objects.create(sender=sender_obj,reciever=reciever_obj,
                                       transaction_id=data['transaction_id'])
            serializer = TransactionSerializer(trans_obj)
            return Response({"success":True,"message":"Transaction captured successfully","data":serializer.data},
                            status=status.HTTP_200_OK)
        except:
            return Response({"success":False,"message":"Error"},status=status.HTTP_200_OK)

