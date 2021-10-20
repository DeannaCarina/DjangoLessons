from django.shortcuts import render
from .models import Item
# Create your views here.


def get_to_do_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'to_do/to_do_list.html', context)
