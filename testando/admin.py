from django.contrib import admin
from testando.models import PedidoPlaca, PedidoLente

# Register your models here.

@admin.register(PedidoPlaca)
class PedidoPlacaAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'status'
    list_display_links = 'name',
    search_fields = 'id', 'name', 'status'
    list_per_page = 10
    ordering = '-id',

@admin.register(PedidoLente)
class PedidoLenteAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'status'
    list_display_links = 'name',
    search_fields = 'id', 'name', 'status'
    list_per_page = 10
    ordering = '-id',