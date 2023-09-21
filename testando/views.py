from django.shortcuts import render
from testando.models import Pedidos

# Create your views here.

def index(request):
    status = request.GET.get('status', 'Aguardando início')  # Default to 'Aguardando início'
    pedidos = Pedidos.objects.filter(status=status)
    
    pedidos_JS = Pedidos.objects.all()
    status_JS = 'Arquivado'
    
    return render(
        request,
        'testando/index.html',
        {
            'pedidos': pedidos,
            'status': status,
            'pedidos_JS': pedidos_JS,
            'status_JS': status_JS,
        }
    )