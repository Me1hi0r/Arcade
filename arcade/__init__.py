from . import mqtt
from .mqtt import mqtt_routine
from time import sleep
from django.core.wsgi import get_wsgi_application
import django
import os

default_app_config = 'arcade.apps.MqttConfig'
# django.setup()
# # print('mqtt start')

# print("Starting Rango population script...")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArcadeServer.settings')
# application = get_wsgi_application()
# # # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArcadeServer.settings')
# django.setup()
# mqtt_routine()
