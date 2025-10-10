from abc import ABC, abstractmethod

from EjercicioIncorrecto.Aves import Ave

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass
    def respirar(self):
        pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass
     
class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        pass

class Aguila(AveVoladora):
    def volar(self):
        print("Aguila está volando")

    def comer(self):
        print("Aguila está comiendo")
    
    def respirar(self):
        print("Aguila está respirando")

class Paloma(AveVoladora):
    def volar(self):
        print("Paloma está voplando")
    def comer(self):
        print("Paloma está comiendo")
    def respirar(self):
        print("Paloma está respirando")

class Pinguino(AveNadadora):
    def comer(self):
        print("Pinguino está comiendo")
    def respirar(self):
        print("Pinguino está respirando")
    def nadar(self):
        print("Pinguino está nadando")

a1 = Aguila()
pa1 = Paloma()
p1 = Pinguino()

a1.comer()
a1.volar()
a1.respirar()

pa1.comer()
pa1.volar()
pa1.respirar()

p1.comer()
p1.volar()
p1.respirar()