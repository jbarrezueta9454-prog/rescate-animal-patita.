import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from patterns.singleton.gestor_casos import GestorCasos
from patterns.singleton.conexion_db import ConexionDB
from patterns.factory.expediente_factory import FABRICAS
from model.usuario import Voluntario
from model.estado import EstadoCaso
from model.animal import Perro, Gato, FaunaSilvestre


class TestPatrones(unittest.TestCase):
    def test_singleton(self):
        self.assertIs(GestorCasos(), GestorCasos.get_instancia())
        self.assertIs(ConexionDB(), ConexionDB())

    def test_factory(self):
        datos = {"nombre": "X", "descripcion": "d", "ubicacion": "u"}
        self.assertIsInstance(FABRICAS["perro"].crear_expediente(datos).animal, Perro)
        self.assertIsInstance(FABRICAS["gato"].crear_expediente(datos).animal, Gato)
        self.assertIsInstance(FABRICAS["fauna"].crear_expediente(datos).animal, FaunaSilvestre)

    def test_observer_y_estados(self):
        gestor = GestorCasos()
        vol = Voluntario(1, "Ana", "a@a.com")
        gestor.suscribir(vol)
        caso = gestor.registrar_caso(
            {"especie": "gato", "nombre": "Misi", "descripcion": "d", "ubicacion": "u"}
        )
        gestor.cambiar_estado(caso.id, EstadoCaso.RESCATADO, vol)
        self.assertEqual(caso.estado, EstadoCaso.RESCATADO)
        with self.assertRaises(ValueError):
            gestor.cambiar_estado(caso.id, EstadoCaso.ADOPTADO, vol)


if __name__ == "__main__":
    unittest.main()
