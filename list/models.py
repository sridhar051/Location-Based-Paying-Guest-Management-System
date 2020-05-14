from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.


class pghotels(models.Model):

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    location=models.TextField()


class userdetailsxx(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, primary_key=True)
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
    def __str__(self):
        return self.user.username
