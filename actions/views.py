from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from post_pic.models import Pic

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name  = request.POST['first_name']
        second_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists.')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=second_name) 
                user.save()
                return redirect('signin') 
        elif len(password) < 8:
            messages.error(request,'Password must be greater than 8 character')
            return redirect('signup')

            
        else:
            messages.error(request,'Password Does Not Match')
            return redirect('signup')

    
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:

            messages.error(request,'Invalid Credentials')
            redirect('signin')
    return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    

    return redirect('/')

def contact(request):
    return render(request,'contact.html')

def user(request,user):
    if request.user.is_authenticated:
        if User.objects.filter(username=user):
            pics = Pic.objects.filter(user=user)
            obj = User.objects.get(username=user)
            

          

            
           
           
        
            return render(request,'user.html',{
            'pics':pics,
            'first_name':obj.first_name,
            'last_name': obj.last_name,
            'username': obj.username,
            
            })
        else:
            messages.error(request,'No user Found')
    else:
        return redirect('signin')
       
    return render(request,'user.html')

def accounts(request):
    return render(request,'accounts.html')
