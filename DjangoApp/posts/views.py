from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    # Retrieve all posts and order them by 'date' field in descending order.
    posts = Post.objects.all().order_by('-date')  # '-' indicates descending order
    return render(request, 'posts/posts_list.html', {'posts': posts})

# Correct indentation for post_page function
def post_page(request, slug):
    # Retrieve a single post using the slug
    post = Post.objects.get(slug=slug) 
    return render(request, 'posts/posts_page.html', {'post': post})

# Ensure the @login_required decorator and function are correctly indented
@login_required(login_url='/users/login/')
def post_new(request):
    return render(request, 'posts/post_new.html')
