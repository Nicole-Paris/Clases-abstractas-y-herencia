from Descuento import Descuento

class CalculadoraDescuentos:
    def calcular(self, tipo: str, precio: float , descuento: Descuento) -> float:
        return descuento.aplicar(precio)