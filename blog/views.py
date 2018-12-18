from django.shortcuts import render
from .models import Post

# this is blog index
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts' : posts
    })