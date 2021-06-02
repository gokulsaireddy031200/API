from django.db import models

# Create your models here.




class Driver(models.Model):

    name = models.TextField()

    license = models.TextField()