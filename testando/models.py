from django.db import models

# Create your models here.

class PedidoPlaca(models.Model):
    
    STATUS = (
        ('Aguardando início', 'Aguardando início'),
        ('Aguardando aprovacao', 'Aguardando aprovacao'),
        ('Aprovado. Aguardando Setups', 'Aprovado. Aguardando Setups'),
        ('Aguardando produção e envio', 'Aguardando produção e envio'),
        ('Em produção', 'Em produção'),
        ('Aguardando envio', 'Aguardando envio'),
        ('Arquivado', 'Arquivado'),
    )
    
    class Meta:
        verbose_name = 'Placa'
        verbose_name_plural = 'Placas'
        
    name = models.CharField(max_length=65)
    
    status = models.CharField(
    verbose_name="Status",
    max_length=100,
    default="Aguardando início",
    choices=STATUS
    )


class PedidoLente(models.Model):
    STATUS = (
        ('Aguardando início', 'Aguardando início'),
        ('Aguardando aprovacao', 'Aguardando aprovacao'),
        ('Aprovado. Aguardando Setups', 'Aprovado. Aguardando Setups'),
        ('Aguardando produção e envio', 'Aguardando produção e envio'),
        ('Em produção', 'Em produção'),
        ('Aguardando envio', 'Aguardando envio'),
        ('Arquivado', 'Arquivado'),
    )
    
    class Meta:
        verbose_name = 'Lente'
        verbose_name_plural = 'Lentes'
        
    name = models.CharField(max_length=65)
    
    status = models.CharField(
    verbose_name="Status",
    max_length=100,
    default="Aguardando início",
    choices=STATUS
    )