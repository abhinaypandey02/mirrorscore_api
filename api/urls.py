from django.urls import path
from .views import ping,schedule
urlpatterns=[
    path('ping/',ping), #for ping request
    path('schedule/',schedule) #for adding new scheduled task
]