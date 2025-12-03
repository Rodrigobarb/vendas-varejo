from decimal import Decimal
from typing import List
from Produto import Produto

class Pedido:
    def __init__(self, nrPedido: int, vlTotal: Decimal, vlLiquido: Decimal, produtos: List[Produto]):
        self.nrPedido = nrPedido
        self.vlTotal = vlTotal
        self.vlLiquido = vlLiquido
        self.produtos = produtos

    def __repr__(self):
        return (f"Pedido n. {self.nrPedido} - Total: R$ {self.vlTotal:.2f} | Líquido: R$ {self.vlLiquido:.2f}")