from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('crear_post')
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Se inicia sesion automaticamente al registrarse
            return redirect('lista_post')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

