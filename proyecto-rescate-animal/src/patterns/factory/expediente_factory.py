"""Patrón Factory Method: creación de expedientes según la especie."""
from abc import ABC, abstractmethod
from datetime import date

from model.animal import Perro, Gato, FaunaSilvestre


class Expediente:
    def __init__(self, animal, ubicacion):
        self.animal = animal
        self.ubicacion = ubicacion
        self.fecha_ingreso = date.today()
        self.tratamientos = []


class ExpedienteFactory(ABC):
    def crear_expediente(self, datos: dict) -> Expediente:
        animal = self.crear_animal(datos)  # Factory Method
        return Expediente(animal, datos["ubicacion"])

    @abstractmethod
    def crear_animal(self, datos: dict):
        ...


class PerroFactory(ExpedienteFactory):
    def crear_animal(self, datos):
        return Perro(datos["nombre"], datos["descripcion"])


class GatoFactory(ExpedienteFactory):
    def crear_animal(self, datos):
        return Gato(datos["nombre"], datos["descripcion"])


class FaunaSilvestreFactory(ExpedienteFactory):
    def crear_animal(self, datos):
        return FaunaSilvestre(
            datos["nombre"], datos["descripcion"], datos.get("cientifico", "")
        )


FABRICAS = {
    "perro": PerroFactory(),
    "gato": GatoFactory(),
    "fauna": FaunaSilvestreFactory(),
}
