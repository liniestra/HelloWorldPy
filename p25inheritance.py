class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

perro = Perro("Rex", 5)
gato = Gato("Jack", 3)
perro.hacer_sonido()
gato.hacer_sonido()
