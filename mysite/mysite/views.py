from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
from home.models import LOGIN
from home.models import Package
from home.models import Booking


def home(request):
   packagedata = Package.objects.all()

   data = {
           'packagedata':packagedata
   }
    
   return render(request,'index.html',data)


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
        
    return render(request,'index.html')



def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        login = LOGIN(email=email,password=password)
        login.save()

    return render(request,'index.html')


