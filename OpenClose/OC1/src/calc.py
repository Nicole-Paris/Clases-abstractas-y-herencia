from DescuentoNavidad import DescuentoNavidad
from DescuentoClienteFrecuente import DescuentoClienteFrecuente
from CalculadoraDescuentos import CalculadoraDescuentos

calc = CalculadoraDescuentos()

print(calc.calcular("descuento unico", 100, DescuentoNavidad()))
print(calc.calcular("cliente frecuente", 100, DescuentoClienteFrecuente()))