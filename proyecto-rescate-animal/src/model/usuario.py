from patterns.observer.observador import Observador


class Usuario(Observador):
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo


class Voluntario(Usuario):
    def actualizar(self, evento):
        print(
            f"[Notif a Voluntario {self.nombre}] {evento['tipo']}: "
            f"caso #{evento['caso_id']} ({evento['especie']})"
        )


class Veterinario(Usuario):
    def actualizar(self, evento):
        print(
            f"[Notif a Veterinario {self.nombre}] {evento['tipo']}: "
            f"caso #{evento['caso_id']} ({evento['especie']})"
        )

    def registrar_tratamiento(self, caso, detalle):
        caso.expediente.tratamientos.append((self.nombre, detalle))


class Administrador(Usuario):
    def actualizar(self, evento):
        print(
            f"[Notif a Admin {self.nombre}] {evento['tipo']}: "
            f"caso #{evento['caso_id']}"
        )
