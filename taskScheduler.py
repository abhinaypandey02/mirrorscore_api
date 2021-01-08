#adding django environment to access django models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mirrorscore_api.settings")
import django
django.setup()

from django.utils import timezone #to get current time
from api.models import Task #the task model
import requests #for the GET requests
def check_for_tasks():
    while True: #infinite loop to keep checking for task
        for task in Task.objects.all():
            if(timezone.now()>=task.time): #checking if any task's time has come
                get_request(task.url) #function to send a get request
                task.delete() #deleting the task as it has been completed (for efficiency)

def get_request(url):
    try:
        requests.get(url) #the get request
    except Exception as e:
        print(e) #for errros like invalid url


