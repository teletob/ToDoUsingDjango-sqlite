from django.db import models

# Create your models here.
class todomodel(models.Model):
  title = models.CharField(max_length=255)
  datetime = models.DateTimeField()
  add_datetime = models.DateTimeField(auto_now=True)