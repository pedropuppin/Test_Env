from django.contrib import admin
from testando.models import Pedidos

# Register your models here.

@admin.register(Pedidos)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'status'
    list_display_links = 'name',
    search_fields = 'id', 'name', 'status'
    list_per_page = 10
    ordering = '-id',