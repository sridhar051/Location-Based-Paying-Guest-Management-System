from django.shortcuts import render
from .models import pghotels
from .models import userdetailsxx
from django.contrib.auth.models import User,auth
# Create your views here.


def pglist(request):
    if request.method=='POST':
        loc=request.POST['search']
        dests=pghotels.objects.filter(location=loc)
        return render(request, "pglist.html", {'dests': dests})


    dests=pghotels.objects.all()

    return render(request, "pglist.html", {'dests': dests})

def pglists(request):

    if request.method=='POST':
        ht=request.POST['hotels']
        return render(request, "pay.html", {'hotel': ht})


    dests=pghotels.objects.all()
    return render(request, "pglist.html", {'dests': dests})



def map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1Ijoic3JpZGhhcjAwMDciLCJhIjoiY2s3b2lra3N4MDVyNzNmbXNsZGZsY2htdiJ9.QGZpr-aeWNBms5QBmdHEUA'
    return render(request, 'map.html',
                  { 'mapbox_access_token': mapbox_access_token })

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

        #x=userdetails.objects.filter(user_id=(request.user).id)

        details=userdetailsxx.objects.create(user_id=(request.user).id,firstname=fname,lastname=lname,email=email,pno=tel,room=rtype,guest=guest,adate=adate,time=time,ddate=ddate,gender=gender,selhotel=selhot)
        details.save();
        return render(request,"razorpay.html")
    else:
        return render(request, "pay.html")
