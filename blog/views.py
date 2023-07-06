from django.shortcuts import render
from blog.data import posts
# Create your views here.


def blog(request):

    context = {
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):

    context = {
        'text': 'Estamos no exemplo',
        'title': 'Essa é uma pagina de exemplo - ',
    }

    return render(
        request,
        'exemplo.html',
        context
    )
