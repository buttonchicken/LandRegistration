from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import *
from django.utils import timezone
from .tasks import mail_otp
from django.db import IntegrityError

class SendOTP(APIView):
    def post(self,request):
        email = request.data['email']
        resp = mail_otp.delay(email)
        Otp.objects.filter(email_id=email).delete()
        otp = resp.get()
        if otp!="":
            otp_obj = Otp()
            otp_obj.value = otp
            otp_obj.email_id = email
            otp_obj.save()
            user_obj = User.objects.filter(email=email)
            if len(user_obj)==0:
                return Response({'message':'OTP Sent successfully','existing user':False,'otp':str(otp)},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message':'OTP Sent successfully','existing user':True,'otp':str(otp)},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'message':'Internal error, Please try again later'},status=status.HTTP_400_BAD_REQUEST)

class Authorize(APIView):
    def post(self,request):
        data = request.data
        email = data['email']
        otp = data['otp']
        exisiting = data['existing_user']
        otp_objs = Otp.objects.filter(email_id = email)
        if str(otp_objs[0].value) == str(otp) and timezone.now() < otp_objs[0].valid_upto:
            #valid otp
            if not exisiting:
                try:
                    RegisterSerializer(data=request.data).is_valid(raise_exception=True)
                    user_object = User.objects.create(username=data['mobile_number'],Aadhaar_no=data['aadhaar_no'],
                                                      mobile_number=data['mobile_number'],first_name=data['first_name'],
                                                      last_name=request.data['last_name'],email=data['email'],
                                                      DOB=data['dob'])
                    user = user_object
                    refresh = RefreshToken.for_user(user)
                    serializer = UserSerailizer(user)
                    Otp.objects.get(value = otp).delete()
                    return Response({"success": True, "message": "Login successful",
                                        'payload': serializer.data,
                                        'refresh': str(refresh),
                                        'access': str(refresh.access_token)},
                                        status=status.HTTP_202_ACCEPTED)
                except KeyError:
                    return Response({'message':'Please enter your First Name, Last Name, Aadhaar No and DOB !!'},status=status.HTTP_400_BAD_REQUEST)
                except IntegrityError:
                    return Response({'message':'User with same aadhaar no. or mobile number exists !!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.get(email=email)
                serializer = UserSerailizer(user)
                refresh = RefreshToken.for_user(user)
                Otp.objects.get(value = otp).delete()
                return Response({"success": True, "message": "Login successful",
                                    'payload': serializer.data,
                                    'refresh': str(refresh),
                                    'access': str(refresh.access_token)},
                                    status=status.HTTP_202_ACCEPTED)
        else:
            #invalid otp
            return Response({"success":False, "message":"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)

