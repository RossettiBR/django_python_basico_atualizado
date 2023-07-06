from django.shortcuts import render
# Create your views here.


def blog(request):

    context = {
         'text': 'Estamos no blog'
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
