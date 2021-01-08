"""
WSGI config for mirrorscore_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mirrorscore_api.settings')

application = get_wsgi_application()

#processess to start at the start of server

import multiprocessing #for multiprocessing
from taskScheduler import check_for_tasks #importing the function to check for due tasks
p1 = multiprocessing.Process(target=check_for_tasks) #creating new process to check for scheduled tasks
p1.start() #starting the process
