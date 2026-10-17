"""Patrón Singleton: una única conexión a la base de datos."""


class ConexionDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conectado = True  # aquí iría la conexión real
        return cls._instancia

    def ejecutar(self, consulta):
        print(f"[DB] {consulta}")
