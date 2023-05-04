from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from menus.models import Menu


# Create your views here.
def index(request):
    context = dict()
    menus = Menu.objects.all()
    today = datetime.now().date()
    context = {'today':today}
    context['menus'] = menus
    return render(request, 'menus/index.html',context)

def detail_view(request,pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu
    return render(request, 'menus/detail.html',context)
