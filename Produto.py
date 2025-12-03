from decimal import Decimal

class Produto:
    def __init__(self, cdProduto: int, nmProduto: str, vlUnitario: Decimal):
        self.cdProduto = cdProduto
        self.nmProduto = nmProduto
        self.vlUnitario = vlUnitario

    def __repr__(self):
        return(f"Produto(nome='{self.nmProduto}', valor={self.vlUnitario})")