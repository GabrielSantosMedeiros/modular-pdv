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

    

class ItemCarrinho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    produto = models.ForeignKeyField(model=Produto)
    quantidade = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        database = provider.getDatabase()
        table_name = 'item_carrinho'


