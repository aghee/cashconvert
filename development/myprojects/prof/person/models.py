from django.db import models
class edu(models.Model):
    primary=models.CharField(max_length=100)
    sec=models.CharField(max_length=100)
    almamater=models.CharField(max_length=100,verbose_name='AlmaMater')
    period=models.DateTimeField()


# Create your models here.
