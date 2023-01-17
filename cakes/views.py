from django.shortcuts import render
from django.http import HttpResponse

from cakes.models import Frozen_cakes,Birthday_cakes, Alfajores
from cakes.forms import Birthday_cakesForm, AlfajoresForm



def index(request):
    return render(request,'index.html',context={})

def create_cake(request):
    if request.method =='GET':
       return render(request, 'create_cake.html', context={})
    
    elif request.method == 'POST':
        Frozen_cakes.objects.create(name=request.POST['name'], price= request.POST['price'])
        return render(request,'create_cake.html', context={})



def list_cakes(request):
    if 'search' in request.GET:
        search = request.GET['search']
        cakes = Frozen_cakes.objects.filter(name__contains=search)
    else:
        cakes = Frozen_cakes.objects.all()
    context = {
        'cakes':cakes,
    }
    return render(request, 'list_cakes.html', context=context)


def create_birthday(request):
   if request.method == 'GET':
       context = {
           'form': Birthday_cakesForm()
       }
       return render(request,'create_birthday.html', context=context)
   
   elif request.method == 'POST':
       form = Birthday_cakesForm(request.POST)
       if form.is_valid():
           Birthday_cakes.objects.create(
               name=form.cleaned_data['name'],
               price=form.cleaned_data['price'],
               stock=form.cleaned_data['stock'],)
           return render(request, 'create_birthday.html', context={})
       else:
            context = {
                'form_errors' : form.errors,
                'form': Birthday_cakesForm()
            }
            return render(request, 'create_birthday.html', context=context)
       
       
       
def list_birthday(request):
    all_birthday = Birthday_cakes.objects.all()
    context = {
        'birthday' : all_birthday
        }
    return render(request, 'list_birthday.html',context=context )


def create_alfajores(request):
   if request.method == 'GET':
       context = {
           'form': AlfajoresForm()
       }
       return render(request,'create_alfajores.html', context=context)
   
   elif request.method == 'POST':
       form = AlfajoresForm(request.POST)
       if form.is_valid():
           Alfajores.objects.create(
               name=form.cleaned_data['name'],
               price=form.cleaned_data['price'],
               stock=form.cleaned_data['stock'],)
           return render(request, 'create_alfajores.html', context={})
       else:
            context = {
                'form_errors' : form.errors,
                'form': AlfajoresForm()
            }
            return render(request, 'create_alfajores.html', context=context)
        
        
def list_alfajores(request):
    all_alfajores = Alfajores.objects.all()
    context = {
        'alfajores' : all_alfajores
    }
    return render(request,'list_alfajores.html', context=context)

