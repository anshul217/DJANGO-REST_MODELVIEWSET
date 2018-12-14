from django.db import models


# Create your models here.

class Inventory(models.Model):
  name = models.CharField(max_length=100, default="")
  price = models.IntegerField(default=0)
  quantity = models.IntegerField(default=0)
