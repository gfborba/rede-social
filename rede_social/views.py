from django.shortcuts import render
from .models import Post, Friendship

def index(request):
    posts = Post.objects.all().order_by('-id')

    friendship = Friendship.objects.filter(user=request.user).first()
    friends = friendship.friends.all()

    return render(request, 'pages/index.html', {'posts':posts,'friends': friends})

