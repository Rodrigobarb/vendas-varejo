from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nmPessoa: str, cdPessoa: int, nmCliente: str, cdCliente: int):
        super().__init__(nmPessoa, cdPessoa)
        self.nmCliente = nmCliente
        self.cdCliente = cdCliente

    # Métodos do seu diagrama
    def cadastro(self):
        print(f"Cliente {self.nmCliente} cadastrado.")

    def fazerPedido(self):
        print(f"Cliente {self.nmCliente} iniciando um pedido.")