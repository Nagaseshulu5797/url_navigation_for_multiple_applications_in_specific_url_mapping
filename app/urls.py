from django.urls import path

from app.views import *

app_name='seshu'

urlpatterns=[
    path('hai/',hai,name='hai'),
]