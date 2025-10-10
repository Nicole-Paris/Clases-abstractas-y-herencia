class Animal:
    def hablar(self):
        raise notImplementedError ("Función no implementada")
    
class Perro(Animal):
    def hablar(self): return "Guau"

class Gato(Animal):
    def hablar(self): return "Miau"

def saludar(animal):
    print (animal.hablar())



class caja(Self):
    def __init__(self, x):
        self._items = []
    def meter(self, x):
        self._items.append(x)
    def primero(self):
        return self._items[0]
    
class MedidorEnergia:
    def energia(self, a:Animal) -> float:
        return len(a.hablar()) * 1.0
        
def describir (a):
    if(isinstance(a,Perro)):
        return "Es un perro" 
    elif isinstance(a,Gato):
        return "Es un gato"
    else:
        return "Animal"
 
saludar(Perro())
saludar(Gato())
c1 = caja(1)
c1.meter(Perro())
c1.meter(Gato())
print(c1.primero())

m = MedidorEnergia()
x=2
print(m.energia(c1.primero()))
