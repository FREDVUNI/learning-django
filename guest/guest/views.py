from django.shortcuts import render,redirect
from . models import Comment
from . forms import commentForm

def index(request):
    comments = Comment.objects.order_by('-date_added') 
    context ={'comments':comments}
    return render(request,"guest/index.html",context)


def sign(request):
    if request.method == 'POST':
        form = commentForm(request.POST or None)
        if form.is_valid():
            content = Comment(name = request.POST['name'],comment = request.POST['comment'])
            content.save()
            return redirect('index')
    else:        
        form = commentForm()
        context ={'form':form}
        return render(request,"guest/sign.html",context)    