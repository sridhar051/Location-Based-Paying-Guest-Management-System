from django.db import models
from django.contrib.auth.models import User,auth

class userdetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    pno=models.IntegerField()
    room=models.CharField(max_length=100)
    guest=models.CharField(max_length=100)
    adate=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    ddate=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    selhotel=models.CharField(max_length=100)
