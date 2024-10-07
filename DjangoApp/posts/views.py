from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_list(request):
    # Retrieve all posts and order them by 'date' field in descending order.
    posts = Post.objects.all().order_by('-date')  # '-' indicates descending order
    return render(request, 'posts/posts_list.html', {'posts': posts})

# Correct indentation for post_page function
def post_page(request, slug):
    # Retrieve all posts and order them by 'date' field in descending order.
    post = Post.objects.get(slug=slug) 
    return render(request, 'posts/posts_page.html', {'post': post})

