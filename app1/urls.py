from django.urls import path

from app1.views import *

app_name='sagar'

urlpatterns=[
    path('hello/',hello,name='hello'),
]