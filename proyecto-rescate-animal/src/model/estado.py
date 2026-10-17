from enum import Enum


class EstadoCaso(Enum):
    REPORTADO = 1
    RESCATADO = 2
    EN_TRATAMIENTO = 3
    DISPONIBLE_ADOPCION = 4
    ADOPTADO = 5
    LIBERADO = 6


# Transiciones válidas entre estados
TRANSICIONES = {
    EstadoCaso.REPORTADO: {EstadoCaso.RESCATADO},
    EstadoCaso.RESCATADO: {EstadoCaso.EN_TRATAMIENTO},
    EstadoCaso.EN_TRATAMIENTO: {EstadoCaso.DISPONIBLE_ADOPCION, EstadoCaso.LIBERADO},
    EstadoCaso.DISPONIBLE_ADOPCION: {EstadoCaso.ADOPTADO},
    EstadoCaso.ADOPTADO: set(),
    EstadoCaso.LIBERADO: set(),
}
