from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/', views.posts_create, name='crear_post'),
    path('posts/', views.posts_list, name='lista_post'),
     path('posts/<int:post_id>/', views.posts_detail, name='detalle_post')
    # Otras URLs...
]