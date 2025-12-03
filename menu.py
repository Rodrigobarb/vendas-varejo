from decimal import Decimal
from typing import List, Dict, Optional

from Cliente import Cliente
from Produto import Produto
from Pedido import Pedido
from Carrinho import Carrinho

from promocao.promocao_strategy import PromocaoStrategy
from promocao.promocao_black_friday import PromocaoBlackFriday
from promocao.promocao_valor import PromocaoValor

class Menu:
    def __init__(self):
        self.promocoes: Dict[str, PromocaoStrategy] = {}
        self.historico_pedidos: List[Pedido] = []
        self.contador_pedidos = 1
        self.cliente_atual: Optional[Cliente] = None
        self.produtos_disponiveis: List[Produto] = []

        self._inicializar_mocks()

    def _inicializar_mocks(self):
        self.cliente_atual = Cliente(
            nmPessoa="Fulano da Silva",
            cdPessoa=1,
            nmCliente="Fulano",
            cdCliente=100
        )
        self.cliente_atual.cadastro()

        prod_tv = Produto(10, "Smart TV 50", Decimal("2000.00"))
        prod_cel = Produto(20, "Smartphone", Decimal("1000.00"))
        prod_fone = Produto(30, "Fone Bluetooth", Decimal("250.00"))
        prod_mouse = Produto(40, "Mouse Gamer", Decimal("150.00"))

        self.produtos_disponiveis = [
            prod_tv, prod_cel, prod_fone, prod_mouse
        ]

    def cadastrar_promocao(self, tipo: str, cupom: str) -> bool:
        if tipo == "1":
            self.promocoes[cupom] = PromocaoBlackFriday()
            return True
        elif tipo == "2":
            self.promocoes[cupom] = PromocaoValor()
            return True
        return False

    def buscar_cupom(self, cupom: str) -> Optional[PromocaoStrategy]:
        return self.promocoes.get(cupom)

    def get_produto_por_indice(self, indice_ajustado: int) -> Optional[Produto]:
        if 0 <= indice_ajustado < len(self.produtos_disponiveis):
            return self.produtos_disponiveis[indice_ajustado]
        return None

    def finalizar_pedido(self, carrinho: Carrinho) -> Optional[Pedido]:
        if not carrinho.produtos:
            return None
        
        pedido = carrinho.finalizarCompra(self.contador_pedidos)
        self.historico_pedidos.append(pedido)
        self.contador_pedidos += 1
        return pedido