"""Patrón Observer: interfaces Observador y Sujeto."""
from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento: dict) -> None:
        ...


class Sujeto(ABC):
    @abstractmethod
    def suscribir(self, obs: Observador) -> None:
        ...

    @abstractmethod
    def desuscribir(self, obs: Observador) -> None:
        ...

    @abstractmethod
    def notificar(self, evento: dict) -> None:
        ...
