from database.core import DatabaseProvider
from database.models import Produto, Carrinho, ItemCarrinho, Pagamento
from database.services import ProdutoService

data_provider = DatabaseProvider()

if __name__ == '__main__':
    data_provider.setTables(Produto, Carrinho, ItemCarrinho, Pagamento)
