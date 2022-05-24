from django.shortcuts import render
from . models import Post,Comment,Category
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def blogindex(request):
    template_name ="blog/index.html"
    posts = Post.objects.all().order_by('-created_on') 
    context ={"posts":posts}
    return render(request,template_name,context)


def blogdetails(request,blogid):
    template_name ="blog/details.html"
    post = Post.objects.get(pk=blogid)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =Comment(
            author =form.cleaned_data['author'],
            body = form.cleaned_data['body'],
            post =post
        )
        comment.save()
        messages.success(request,('Your comment has been added.'))
    comments = Comment.objects.filter(post=post)
    context ={"post":post,"comments":comments,"form":form}
    return render(request,template_name,context)

def category(request,category):
    template_name ="blog/category.html"
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(categories__name__contains =category)
    context ={"posts":posts,"category":category}
    return render(request,template_name,context)



