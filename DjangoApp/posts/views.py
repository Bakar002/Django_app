from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import  forms

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
# def post_new(request):
#     return render(request, 'posts/posts_new.html')


def post_new(request):
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })











    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)  # Use request.FILES for image uploads
    #     if form.is_valid():
    #         form.save()
    #         return redirect('post_list')  # Redirect to the post list or any other view
    # else:
    #     form = PostForm()
    
    # return render(request, 'add_post.html', {'form': form})

