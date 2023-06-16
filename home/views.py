from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render , HttpResponse
from home.models import ContactData
from datetime import datetime
from Blog.models import BlogView, Blog
from django.db import models
from django.contrib.auth.decorators import login_required

def home(request):

    most_viewed = BlogView.objects.order_by('-views')[:10]

    recent_blogs = Blog.objects.order_by('-datetime')[:10]

    context = {
        'most_viewed': most_viewed,
        'recent_blogs': recent_blogs
    }

    return render(request, 'Home/home.html', context)


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

@login_required
def profile_view(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
    }
    print("okk")
    return render(request, 'Home/viewProfile.html', context)

# @login_required
# def profile_update_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         avatar = request.FILES.get('avatar')
        
#         # Perform validation and save the updated profile data
#         user = request.user
#         user.email = email
#         if avatar:
#             user.avatar = avatar
#         user.save()
        
#         # Redirect to the profile page after updating
#         return redirect('account:profile')

#     # GET request, render the profile update form
#     user = request.user
#     context = {
#         'username': user.username,
#         'email': user.email,
#     }
#     return render(request, 'account/profile_update.html', context)

def profile_update_view():
    return HttpResponse('<div><h1>This is Under construction</h1><br><a href="/">GO back</a></div>')

