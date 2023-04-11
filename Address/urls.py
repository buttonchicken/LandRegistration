from django.urls import path,include
from .views import *

urlpatterns = [
    path('insert',Insert_Address.as_view()),
]
