import peewee as models
import uuid
from datetime import datetime
from database.core import DatabaseProvider


provider = DatabaseProvider()


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    descricao = models.TextField()
    imagem = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        database = provider.getDatabase()
        table_name = 'produtos'



class Carrinho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cliente = models.CharField(max_length=255, null=True)
    contato = models.TextField(null=True)
    endereco = models.TextField(null=True)
    status_entrega = models.CharField(default='PENDENTE')
    status_pagamento = models.CharField(default='PENDENTE')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        database = provider.getDatabase()
        table_name = 'carrinho'

    

class ItemCarrinho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    carrinho = models.ForeignKeyField(model=Carrinho, backref='itens')
    produto = models.ForeignKeyField(model=Produto)
    quantidade = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        database = provider.getDatabase()
        table_name = 'item_carrinho'



class Pagamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    carrinho = models.ForeignKeyField(model=Carrinho, backref='pagamentos')
    tipo_pagamento = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_comprovante = models.TextField(null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        database = provider.getDatabase()
        table_name = 'pagamentos'