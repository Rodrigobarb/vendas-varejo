from decimal import Decimal
from .promocao_strategy import PromocaoStrategy

# Herança e Strategy
class PromocaoValor(PromocaoStrategy):
    def __init__(self):
        self.prDesconto: Decimal = Decimal("10.0") # R$ 10,00 fixos

    def calcularDesconto(self, desconto: Decimal) -> Decimal:
        valor_total_bruto = desconto
        valor_do_desconto = self.prDesconto

        #valida
        if valor_do_desconto > valor_total_bruto:
            return valor_total_bruto
        return valor_do_desconto