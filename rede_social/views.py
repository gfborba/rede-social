from django.shortcuts import render
from .models import Post, Friendship, Invite

def index(request):
    posts = Post.objects.all().order_by('-id')

    friendship = Friendship.objects.filter(user=request.user).first()
    friends = friendship.friends.all()

    return render(request, 'pages/index.html', {'posts':posts,'friends': friends})

# def envio_de_convites(request):
#     pass

#     meus_convites = Invite.objects.filter(reciver_id=request.user)

#     meus_convites.status = "APPROVED"

#     Friendship.objects.create(
#         sender=meus_convites.sender.
#     )

# def alterar_status(request, id):
#     meus_convites = Invite.objects.filter(id=id)

