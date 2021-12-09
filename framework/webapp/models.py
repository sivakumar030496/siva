from django.db import models

# Create your models here.
class Group(models.Model):
    Branch=models.CharField(max_length=20)

class employees(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    emp_id=models.IntegerField()
    Branch=models.ForeignKey(Group, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100,default=True)
    Address=models.TextField(max_length=100,default=True)
    gender=models.CharField(max_length=10,default=True)
    country=models.CharField(max_length=10,default=True)

def __str__(self):
    return self.firstname