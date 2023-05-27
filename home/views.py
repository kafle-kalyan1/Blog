from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render , HttpResponse
from home.models import ContactData
from datetime import datetime

def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    if request.method == 'POST':
        messageF = request.POST.get('message')
        emailF = request.POST.get('email')
        nameF = request.POST.get('name')
        phoneF = request.POST.get('phone')
        if nameF == '' or phoneF == '' or emailF == '' or messageF == '':
            messages.warning(request, 'Please fill all the required fields')
        else:
            contact = ContactData(name=nameF, email=emailF, phone=phoneF, description=messageF, dateTime=datetime.now())
            contact.save()
            messages.success(request, 'Successfully message was sent')
    return render(request, 'Home/contact.html')