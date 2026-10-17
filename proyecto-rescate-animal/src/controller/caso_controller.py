"""Controlador (MVC): coordina la Vista y el Modelo."""


class CasoController:
    def __init__(self, gestor, vista):
        self.gestor = gestor
        self.vista = vista

    def reportar_rescate(self, datos):
        caso = self.gestor.registrar_caso(datos)
        self.vista.mostrar_caso(caso)
        return caso

    def asignar(self, id_caso, usuario):
        self.gestor.asignar_responsable(id_caso, usuario)
        self.vista.mostrar_mensaje(f"Caso #{id_caso} asignado a {usuario.nombre}")

    def actualizar_estado(self, id_caso, estado, usuario):
        self.gestor.cambiar_estado(id_caso, estado, usuario)
        self.vista.mostrar_mensaje(f"Caso #{id_caso} ahora está en {estado.name}")
