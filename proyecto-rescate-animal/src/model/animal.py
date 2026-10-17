from abc import ABC, abstractmethod


class Animal(ABC):
    """Clase base abstracta de los animales rescatados."""

    especie = "Animal"

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    @abstractmethod
    def cuidados_especiales(self):
        ...

    @abstractmethod
    def requisitos_adopcion(self):
        ...


class Perro(Animal):
    especie = "Perro"

    def cuidados_especiales(self):
        return "Vacunación, desparasitación, esterilización"

    def requisitos_adopcion(self):
        return "Hogar con espacio, compromiso de paseos"


class Gato(Animal):
    especie = "Gato"

    def cuidados_especiales(self):
        return "Test FeLV/FIV, vacunación, esterilización"

    def requisitos_adopcion(self):
        return "Hogar con ventanas protegidas"


class FaunaSilvestre(Animal):
    especie = "Fauna Silvestre"

    def __init__(self, nombre, descripcion, cientifico=""):
        super().__init__(nombre, descripcion)
        self.nombre_cientifico = cientifico

    def cuidados_especiales(self):
        return "Manejo mínimo, hábitat adecuado, coordinación con autoridad ambiental"

    def requisitos_adopcion(self):
        return "No adoptable: se libera o se deriva a centro especializado"
