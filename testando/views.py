from django.shortcuts import render
from testando.models import Pedidos

# Create your views here.

def index(request):
    pedidos = Pedidos.objects.all()
    status = 'Arquivado'
    
    return render(
        request,
        'testando/index.html',
        {
            'pedidos': pedidos,
            'status': status,
        }
    )