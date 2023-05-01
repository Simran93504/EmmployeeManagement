from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)