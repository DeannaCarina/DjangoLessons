from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_to_do_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'to_do/to_do_list.html', context)

def add_item(request):
    if request.method =="POST":
        name = request.POST.get("item_name")
        done = "done" in request.POST
        Item.objects.create(name=name, done=done)
        return redirect("get_to_do_list")

    return render(request, 'to_do/add_item.html')
