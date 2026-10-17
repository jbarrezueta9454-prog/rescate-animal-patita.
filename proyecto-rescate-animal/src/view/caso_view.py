"""Vista (MVC): solo presenta información, sin lógica de negocio."""


class CasoView:
    def mostrar_caso(self, caso):
        print(
            f"Caso #{caso.id} | {caso.expediente.animal.especie} | "
            f"Estado: {caso.estado.name}"
        )

    def mostrar_mensaje(self, texto):
        print(texto)
