from django.db import models

class Toukou(models.Model):
    title = models.CharField(max_length=200)
    bun = models.CharField(max_length=500)
    
