from decimal import Decimal
from .promocao_strategy import PromocaoStrategy

#Herança e Padrão Adicional (Strategy)
class PromocaoBlackFriday(PromocaoStrategy):
    def __init__(self):
        self.prDesconto: Decimal = Decimal("50.00") 

    def calcularDesconto(self, desconto: Decimal) -> Decimal:
        valor_total_bruto = desconto
        valor_do_desconto = valor_total_bruto * (self.prDesconto / 100)
        return valor_do_desconto