from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/', views.posts_create, name='crear_post'),
    path('posts/', views.posts_list, name='lista_post'),
    # Otras URLs...
]