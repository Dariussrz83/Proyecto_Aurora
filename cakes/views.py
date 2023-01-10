from django.shortcuts import render
from django.http import HttpResponse

from cakes.models import Frozen_cakes,Birthday_cakes, Alfajores

def index(request):
    return render(request,'index.html',context={})

def create_cake(request):
    Frozen_cakes.objects.create(name='Oreo', price=4000, stock= True)
    return HttpResponse('se creo el nuevo producto')

def list_cakes(request):
    all_cakes = Frozen_cakes.objects.all()
    context = {
        'cakes':all_cakes,
    }
    return render(request, 'list_cakes.html', context=context)


def create_birthday(request):
    Birthday_cakes.objects.create(name='Dos rellenos', price=4000, stock= True)
    return HttpResponse ('Torta de cumpleaños creada')

 
def list_birthday(request):
    all_birthday = Birthday_cakes.objects.all()
    context = {
        'birthday' : all_birthday
        }
    return render(request, 'list_birthday.html',context=context )


def create_alfajores(request):
    Alfajores.objects.create(name='Maicena', price=180, stock=False)
    return HttpResponse ('Nuevo alfajor creado')
    
        
def list_alfajores(request):
    all_alfajores = Alfajores.objects.all()
    context = {
        'alfajores' : all_alfajores
    }
    return render(request,'list_alfajores.html', context=context)

