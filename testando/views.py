from django.shortcuts import render
from testando.models import PedidoPlaca, PedidoLente
from testando.forms.peido_filter_form import PedidoFilterForm

# Create your views here.

def index(request):
    pedidos_placa = PedidoPlaca.objects.all()  # Start with all objects
    pedidos_lente = PedidoLente.objects.all()  

    if request.method == 'GET':
        filter_form = PedidoFilterForm(request.GET)
        if filter_form.is_valid():
            status_filter = filter_form.cleaned_data['status_filter']
            if status_filter:
                pedidos_placa = pedidos_placa.filter(status__in=status_filter)
                pedidos_lente = pedidos_lente.filter(status__in=status_filter)
    else:
        filter_form = PedidoFilterForm()

    pedidos = pedidos_placa.union(pedidos_lente, all=True)

    context = {
        'pedidos': pedidos,
        'filter_form': filter_form,
    }

    return render(
        request, 
        'testando/index.html', 
        context
    )

