from django.urls import path,include
from .views import *

urlpatterns = [
    path('send_otp',SendOTP.as_view()),
    path('authorize',Authorize.as_view()),
    path('loginadmin',AdminLogin.as_view()),
]
