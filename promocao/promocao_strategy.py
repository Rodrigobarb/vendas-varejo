from abc import ABC, abstractmethod
from decimal import Decimal

# Abstração
class PromocaoStrategy(ABC):
    # Polimorfismo
    @abstractmethod
    def calcularDesconto(self, desconto: Decimal) -> Decimal:
        pass