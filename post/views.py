from django.shortcuts import render, redirect
from .models import Post

def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('create.html')
    return render(request, 'create.html')


