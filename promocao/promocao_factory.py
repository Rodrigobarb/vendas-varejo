from typing import Optional
from Cliente import Cliente
from .promocao_strategy import PromocaoStrategy
from .promocao_black_friday import PromocaoBlackFriday
from .promocao_valor import PromocaoValor

#Factory
class PromocaoFactory:
    @staticmethod
    def criarPromocao(cliente: Cliente, cupom: str) -> Optional[PromocaoStrategy]:
        if cupom == "BF50":
            return PromocaoBlackFriday()
        elif cupom == "VALOR10":
            return PromocaoValor()
        else:
            return None