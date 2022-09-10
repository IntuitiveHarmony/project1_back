from django.db import models

# Create your models here.

#when updating model, make sure to update serializers.py and views.py
class Sequence(models.Model):
    name = models.CharField(max_length=32, null=True)
