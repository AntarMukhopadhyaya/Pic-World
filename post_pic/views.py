from django.shortcuts import render,redirect
from .models import Pic,Comments
from django.contrib import messages

# Create your views here.
def post(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            img_name = request.POST['img_name']
            tags = request.POST['tags']
            web_link =request.POST['web_link']
            img_desc = request.POST['img_desc']
            img = request.FILES['img']
            pic = Pic(user=user,img_name=img_name,img_desc=img_desc,img=img,tags=tags,web_link=web_link)
            pic.save()
            messages.success(request,'Image Posted Successfully')
            return redirect('post')
            
        return render(request,'post.html')
    return redirect('signin')    

def pic(request,query):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        comment_pic = query
        comments = Comments(user=user,comment=comment,comment_pic=comment_pic)
        comments.save()
        messages.success(request,'Comments Posted Successfully')
        return redirect('/post_pic/pic/'+query)


        
    obj = Pic.objects.get(img_name=query)
    comments = Comments.objects.filter(comment_pic=query)
    print(comments) 
    
  
        
    return render(request,'pic.html',
    {
        'comments':comments,
        'img_name': obj.img_name,
        'img': obj.img,
        
        'tags': obj.tags,
        'desc': obj.img_desc,
        'web_link':obj.web_link,
        'pub_date': obj.pub_date,
        'pub_by': obj.user
    
        }
        )
        

