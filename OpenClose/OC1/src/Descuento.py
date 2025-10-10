class Descuento:
    @abstractmethod
    def aplicar(self , precio: float) -> float:
        pass