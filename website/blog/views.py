from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def homeView(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/index.html', context)

def detailView(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    context = {
        'post' : post
    }
    return render(request, 'blog/detail.html', context)