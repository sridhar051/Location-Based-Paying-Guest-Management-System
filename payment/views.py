from django.shortcuts import render
from .models import userdetails
# Create your views here.


def pay(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        tel=request.POST['pno']
        rtype=request.POST['radio']
        guest=request.POST['optradio']
        adate=request.POST['arrival']
        time=request.POST['time']
        ddate=request.POST['departure']
        gender=request.POST['gender']
        selhot=request.POST['hotelname']

        details=userdetails.objects.create(firstname=fname,lastname=lname,email=email,pno=tel,room=rtype,guest=guest,adate=adate,time=time,ddate=ddate,gender=gender,selhot=selhot)
        details.save();
        return redirect(request,"index.html")
    else:
        return render(request, "pay.html")
