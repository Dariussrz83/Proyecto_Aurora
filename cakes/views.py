from django.shortcuts import render
from django.http import HttpResponse

from cakes.models import Frozen_cakes

def create_cake(request):
    Frozen_cakes.objects.create(name='Oreo', price=4000, stock= True)
    return HttpResponse('se creo el nuevo producto')

def list_cakes(request):
    all_cakes = Frozen_cakes.objects.all()
    context = {
        'cakes':all_cakes,
    }
    return render(request, 'list_cakes.html', context=context)
 
