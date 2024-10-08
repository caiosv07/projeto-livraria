from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from favoritos.models import Favoritos2
from livrariaapp.models import Livros
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist



def home(request):
    livros = Livros.objects.all()
    
    paginator = Paginator(livros, 4)

    page = request.GET.get('page')

    livro = paginator.get_page(page)

    context = {
        'livro':livro
    }

    return render(request, 'livros/home.html', context)

@login_required
def favpage(request):
    try:
        fav = Favoritos2.objects.get(user=request.user)
    except ObjectDoesNotExist:
        pass
    

    context = {
        'fav':fav
    }

    return render(request, 'livros/favpage.html', context)  

@login_required
def livroview(request, id):
    livro =  Livros.objects.get(pk=id)

    context = {
        'livro':livro
    }

    return render(request, 'livros/livroview.html', context)


        
