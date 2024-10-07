from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    # Retrieve all posts and order them by 'date' field in descending order.
    posts = Post.objects.all().order_by('-date')  # '-' indicates descending order
    return render(request, 'posts/posts_list.html', {'posts': posts})
