from django.db import models

class Task(models.Model):#the task model
    url=models.CharField(max_length=200) #url to send get request
    time=models.DateTimeField() #time to send the request