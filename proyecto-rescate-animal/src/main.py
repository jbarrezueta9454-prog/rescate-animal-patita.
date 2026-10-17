"""Demostración del Sistema de Rescate y Adopción Animal.
Ejecutar desde la carpeta src:  python main.py
"""
from patterns.singleton.gestor_casos import GestorCasos
from model.usuario import Voluntario, Veterinario, Administrador
from model.estado import EstadoCaso
from controller.caso_controller import CasoController
from view.caso_view import CasoView

gestor = GestorCasos.get_instancia()
assert gestor is GestorCasos(), "Singleton: debe ser la misma instancia"

vol = Voluntario(1, "Ana", "ana@mail.com")
vet = Veterinario(2, "Dr. Luis", "luis@mail.com")
admin = Administrador(3, "Marta", "marta@mail.com")
gestor.suscribir(vol)
gestor.suscribir(vet)
gestor.suscribir(admin)

ctrl = CasoController(gestor, CasoView())

print("\n--- 1. Un ciudadano reporta un rescate ---")
caso = ctrl.reportar_rescate(
    {
        "especie": "perro",
        "nombre": "Firulais",
        "descripcion": "Herido en la vía",
        "ubicacion": "Portoviejo",
    }
)

print("\n--- 2. El administrador asigna al veterinario ---")
ctrl.asignar(caso.id, vet)

print("\n--- 3. Cambios de estado ---")
ctrl.actualizar_estado(caso.id, EstadoCaso.RESCATADO, vet)
ctrl.actualizar_estado(caso.id, EstadoCaso.EN_TRATAMIENTO, vet)
vet.registrar_tratamiento(caso, "Sutura y antibiótico")
ctrl.actualizar_estado(caso.id, EstadoCaso.DISPONIBLE_ADOPCION, vet)

print("\n--- 4. Fauna silvestre (otra fábrica) ---")
ctrl.reportar_rescate(
    {
        "especie": "fauna",
        "nombre": "Mono aullador",
        "descripcion": "Encontrado en zona urbana",
        "ubicacion": "Manta",
        "cientifico": "Alouatta palliata",
    }
)

print("\n--- 5. Transición inválida (debe fallar) ---")
try:
    ctrl.actualizar_estado(caso.id, EstadoCaso.REPORTADO, vet)
except ValueError as e:
    print("Error controlado:", e)

print("\nHistorial del caso #1:")
for fecha, ant, nuevo, autor in caso.historial:
    print(f"  {fecha:%H:%M:%S} {ant.name} -> {nuevo.name} (por {autor})")
