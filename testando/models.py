from django.db import models

# Create your models here.

class Pedidos(models.Model):
    
    STATUS = (
        ('Aguardando início', 'Aguardando início'),
        ('Arquivado', 'Arquivado'),
    )
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
    name = models.CharField(max_length=65)
    
    status = models.CharField(
    verbose_name="Status",
    max_length=100,
    default="Aguardando início",
    choices=STATUS
    )