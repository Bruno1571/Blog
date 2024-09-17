from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('create.html')
    return render(request, 'create.html')


def posts_list(request):
    nombreAutor = request.GET.get('autor') 
    if nombreAutor:
        posts = Post.objects.filter(Autor=nombreAutor)  
    else:
        posts = Post.objects.all()  
    
    return render(request, 'listaPublicaciones.html', {'posts': posts})



def posts_detail(request, post_id):
    # Recupera el post usando el ID proporcionado. Si no se encuentra, se muestra un error 404.
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detallePublicaciones.html', {'post': post})

