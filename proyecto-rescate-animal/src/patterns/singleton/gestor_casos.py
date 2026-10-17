"""Patrón Singleton: único motor de gestión de casos (también es el Sujeto del Observer)."""
import threading

from patterns.observer.observador import Sujeto
from patterns.factory.expediente_factory import FABRICAS
from patterns.singleton.conexion_db import ConexionDB
from model.caso import Caso


class GestorCasos(Sujeto):
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
                    cls._instancia._casos = {}
                    cls._instancia._observadores = []
                    cls._instancia._siguiente_id = 1
        return cls._instancia

    @classmethod
    def get_instancia(cls):
        return cls()

    # ----- Observer (Sujeto concreto) -----
    def suscribir(self, obs):
        if obs not in self._observadores:
            self._observadores.append(obs)

    def desuscribir(self, obs):
        self._observadores.remove(obs)

    def notificar(self, evento):
        for obs in self._observadores:
            obs.actualizar(evento)

    # ----- Lógica de negocio -----
    def registrar_caso(self, datos):
        fabrica = FABRICAS[datos["especie"]]  # Factory Method
        expediente = fabrica.crear_expediente(datos)
        caso = Caso(self._siguiente_id, expediente)
        self._casos[caso.id] = caso
        self._siguiente_id += 1
        ConexionDB().ejecutar(f"INSERT caso {caso.id}")  # Singleton
        self.notificar(
            {
                "tipo": "NUEVO_RESCATE",
                "caso_id": caso.id,
                "especie": expediente.animal.especie,
            }
        )  # Observer
        return caso

    def asignar_responsable(self, id_caso, usuario):
        caso = self._casos[id_caso]
        caso.responsable = usuario
        self.notificar(
            {
                "tipo": "CASO_ASIGNADO",
                "caso_id": id_caso,
                "especie": caso.expediente.animal.especie,
            }
        )

    def cambiar_estado(self, id_caso, estado, usuario):
        self._casos[id_caso].cambiar_estado(estado, usuario)
        ConexionDB().ejecutar(f"UPDATE caso {id_caso} estado={estado.name}")

    def obtener_caso(self, id_caso):
        return self._casos[id_caso]
