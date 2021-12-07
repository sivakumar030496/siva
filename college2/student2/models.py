from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class studentdata(models.Model):

    User=models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    gender_choices=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )


    country_choices=(

        ('AUSTRALIA','AUSTRALIA'),
        ('BANGLADESH','BANGLADESH'),
        ('CHINA','CHINA'),
        ('DENMARK','DENMARK'),
        ('EGYPT','EGYPT'),
        ('INDIA', 'INDIA'),
        ('SWEDEN','SWEDEN'),
        ('USA','USA'),
    )
    group_choices=(
        ('CIVIL','CIVIL'),
        ('MECH','MECH'),
        ('EEE','EEE'),
        ('CSC','CSC')
    )

    name = models.CharField(max_length=19, null=True)
    group = models.CharField(max_length=15, choices=group_choices)
    mobile = models.CharField(max_length=16, null=True)
    email = models.EmailField(null=True)
    password=models.CharField(max_length=8,null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=7,choices=gender_choices)
    country=models.CharField(max_length=15,choices=country_choices)
    marks_percentage=models.FloatField()


    #def __str__(self):
     #   return self.name+str(self.id)
