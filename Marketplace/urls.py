from django.urls import path,include
from .views import *

urlpatterns = [
    path('insert',Insert_Property.as_view()),
    path('view',ViewMarketplace.as_view()),
]
