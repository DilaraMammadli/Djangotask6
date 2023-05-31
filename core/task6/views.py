from django.shortcuts import render
from .models import Product

def infos(request):
    context = {
        "products": Product.objects.all()
    }

    return render(request, "list.html", context)


def create_view(request):
    context = {
        "product": Product.objects.all()
    }

    return render(request, "create.html", context)

def detail_view(request, id):
    context = {
        "id":id,
        "product": Product.objects.get(id=id)
    }

    return render(request, "detail/<id>.html", context)