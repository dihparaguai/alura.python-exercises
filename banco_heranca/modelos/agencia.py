from modelos.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero

    def __str__(self) -> str:
        return f"nome do banco: {self.nome}\nendereco: {self.endereco}\nnumero: {self.numero}"