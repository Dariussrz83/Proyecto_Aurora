from django.shortcuts import render
from django.http import HttpResponse

from cakes.models import Frozen_cakes,Birthday_cakes, Alfajores
from cakes.forms import Birthday_cakesForm, AlfajoresForm,Frozen_cakesForm
from django.views.generic import DeleteView



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

def cakes_update(request,pk):
    frozen_cakes = Frozen_cakes.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Frozen_cakesForm(
                initial={
                    'name':frozen_cakes.name,
                    'price':frozen_cakes.price,
                    'stock':frozen_cakes.stock,
                    
                }
            )
        }

        return render(request, 'update_cakes.html', context=context)

    elif request.method == 'POST':
        form = Frozen_cakesForm(request.POST)
        if form.is_valid():
            frozen_cakes.name = form.cleaned_data['name']
            frozen_cakes.price= form.cleaned_data['price']
            frozen_cakes.stock= form.cleaned_data['stock']
            frozen_cakes.save()
            
            context = {
                'message': 'Torta de cumpleaños actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Frozen_cakesForm()
            }
        return render(request, 'update_cakes.html', context=context)
    
    
    
class Frozen_cakesDeleteView(DeleteView):
    model = Frozen_cakes
    template_name = 'delete_cakes.html'
    success_url = '/cakes/list-cakes/'
        
    

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



def birthday_update(request,pk):
    birthday = Birthday_cakes.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Birthday_cakesForm(
                initial={
                    'name':birthday.name,
                    'price':birthday.price,
                    'stock':birthday.stock,
                    
                }
            )
        }

        return render(request, 'update_birthday.html', context=context)

    elif request.method == 'POST':
        form = Birthday_cakesForm(request.POST)
        if form.is_valid():
            birthday.name = form.cleaned_data['name']
            birthday.price= form.cleaned_data['price']
            birthday.stock= form.cleaned_data['stock']
            birthday.save()
            
            context = {
                'message': 'Torta de cumpleaños actualizada'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Birthday_cakesForm()
            }
        return render(request, 'update_birthday.html', context=context)
    
    
class Birthday_cakesDeleteView(DeleteView):
    model = Birthday_cakes
    template_name = 'delete_birthday.html'
    success_url = '/cakes/list-birthday/'   
    
    
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

def alfajores_update(request, pk):
    alfajores = Alfajores.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': AlfajoresForm(
                initial={
                    'name':alfajores.name,
                    'price':alfajores.price,
                    'stock':alfajores.stock,
                }
            )
        }

        return render(request, 'update_alfajores.html', context=context)

    elif request.method == 'POST':
        form = AlfajoresForm(request.POST)
        if form.is_valid():
            alfajores.name = form.cleaned_data['name']
            alfajores.price= form.cleaned_data['price']
            alfajores.stock= form.cleaned_data['stock']
            alfajores.save()
            
            context = {
                'message': 'Alfajor actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': AlfajoresForm()
            }
        return render(request, 'update_alfajores.html', context=context)

class AlfajoresDeleteView(DeleteView):
    model = Alfajores
    template_name = 'delete_alfajores.html'
    success_url = '/cakes/list-alfajores/'  
    
    
    
def about(request):
    return render(request,'about.html', context={})
