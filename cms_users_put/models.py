from django.db import models


# users: anombela password: anombela

# Create your models here.
class Pages(models.Model):
    name = models.CharField(max_length=32)
    page = models.TextField()