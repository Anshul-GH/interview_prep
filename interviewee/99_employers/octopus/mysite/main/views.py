from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.


def index(response):
    # return HttpResponse("<h1>Learning Django (TWT)</h1>")
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"name": ls.name})


def item(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, item.text))


def home(response):
    return render(response, "main/home.html", {"name": "test"})
