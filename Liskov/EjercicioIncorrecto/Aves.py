from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def nadar(self):
        pass

class Aguila(Ave):
    def volar(self):
        print("Aguila está volando")

    def comer(self):
        print("Aguila está comiendo")

    def nadar(self):
        raise Exception("Aguila no puede nadar")

class Paloma(Ave):
    def volar(self):
        print("Paloma está voplando")
    def comer(self):
        print("Paloma está comiendo")
    def nadar(self):
        print("Paloma está nadando")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Pinguino no puede volar")
    def comer(self):
        print("Pinguino está comiendo")
    def nadar(self):
        print("Pinguino está nadando")

a1 = Aguila()
pa1 = Paloma()
p1 = Pinguino()

a1.comer()
a1.volar()
a1.nadar()

pa1.comer()
pa1.volar()
pa1.nadar()

p1.comer()
p1.volar()  
p1.nadar()