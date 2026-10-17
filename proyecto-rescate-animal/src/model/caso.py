from datetime import datetime

from model.estado import EstadoCaso, TRANSICIONES


class Caso:
    """Caso de rescate: guarda el estado, el responsable y el historial."""

    def __init__(self, id, expediente):
        self.id = id
        self.expediente = expediente
        self.estado = EstadoCaso.REPORTADO
        self.responsable = None
        self.historial = []  # (fecha, estado anterior, estado nuevo, autor)

    def cambiar_estado(self, nuevo, usuario):
        if nuevo not in TRANSICIONES[self.estado]:
            raise ValueError(
                f"Transición inválida: {self.estado.name} -> {nuevo.name}"
            )
        self.historial.append((datetime.now(), self.estado, nuevo, usuario.nombre))
        self.estado = nuevo
