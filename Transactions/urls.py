from django.urls import path,include
from .views import *

urlpatterns = [
    path('capture',Capture_Transaction.as_view()),
]