from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        pass

    @abstractmethod
    def ligar(self):
        pass