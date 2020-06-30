from django.shortcuts import render,redirect
from django.contrib import messages
from post_pic.models import Pic
from django.contrib.auth.models import User

def index(request):
    pics = Pic.objects.all()[0:10]
    
    return render(request,'index.html',{'pics': pics})

def about(request):
    return render(request,'about.html')

def search(request):
    query = request.GET['query']
    alluser = User.objects.filter(username__contains=query)
    allpics = Pic.objects.filter(img_name__contains=query)
    params = {
        'allUser': alluser,
        'allPics':allpics,
        'query': query,
        
        }

    return render(request,'results.html',params)

