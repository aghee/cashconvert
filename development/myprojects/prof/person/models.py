from django.db import models
class edu(models.Model):
    primary=models.CharField(max_length=100)
    sec=models.CharField(max_length=100)
    almamater=models.CharField(max_length=100,verbose_name='AlmaMater')
    period=models.DateTimeField()
    def __str__(self):
        return self.primary
class pdetails(models.Model):
    name=models.CharField(max_length=100)
    DoB=models.DateTimeField()
    residence=models.CharField(max_length=100)
    maritalstatus=models.CharField(max_length=100)
    hobbies=models.TextField(blank=False,null=False)
    def __str__(self):
        return self.name




# Create your models here.
