from django.shortcuts import render,redirect
from django.contrib import messages
from post_pic.models import Pic
from django.contrib.auth.models import User
def index(request):
    if request.method == 'POST':
        user = request.POST['user']
        if User.objects.filter(username=user).exists():
            return redirect('/actions/user/' + user)
        elif Pic.objects.filter(tags=user).exists():
            return redirect('/post_pic/pic'+user)
        else:
            messages.error(request,'No User Found')
            return redirect('/')
        

    
    pics = Pic.objects.all()[0:10]
    
    return render(request,'index.html',{'pics': pics})

def about(request):
    return render(request,'about.html')

