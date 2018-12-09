from django.db import models
from django.utils import timezone

class Honeycomms(models.Model):
    ktshop_url = models.TextField()
    ktshop_source = models.TextField()
    read_datetime = models.DateTimeField(default=timezone.now)