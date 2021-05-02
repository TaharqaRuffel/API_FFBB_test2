from django.test import TestCase

# Create your tests here.
import os

settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
settings_module = os.environ.get("Path")
print(settings_module)