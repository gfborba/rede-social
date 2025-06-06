from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post')
]