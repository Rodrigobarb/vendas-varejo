from decimal import Decimal
from typing import List, Optional
from Produto import Produto
from Pedido import Pedido
from promocao.promocao_strategy import PromocaoStrategy

class Carrinho:
    def __init__(self):
        self.produtos: List[Produto] = []
        self.promocaoAtiva: Optional[PromocaoStrategy] = None

    def adicionarProduto(self, p: Produto):
        self.produtos.append(p)
        print(f"Adicionado: {p.nmProduto}")

    def removerProduto(self, p: Produto):
        if p in self.produtos:
            self.produtos.remove(p)

    def _calcular_total_bruto(self) -> Decimal:
        return sum(p.vlUnitario for p in self.produtos)

    def calcularTotalFinal(self) -> Decimal:
        total_bruto = self._calcular_total_bruto()
        desconto = Decimal("0.00")

        if self.promocaoAtiva:
            desconto = self.promocaoAtiva.calcularDesconto(total_bruto)
        
        return total_bruto - desconto



    def finalizarCompra(self, nrPedido: int) -> Pedido:
        total_bruto = self._calcular_total_bruto()
        total_liquido = self.calcularTotalFinal()
        
        novo_pedido = Pedido(
            nrPedido=nrPedido,
            vlTotal=total_bruto,
            vlLiquido=total_liquido,
            produtos=list(self.produtos)
        )
        
        self.produtos.clear()
        self.promocaoAtiva = None
        return novo_pedido

    def setPromocao(self, p: PromocaoStrategy):
        self.promocaoAtiva = p