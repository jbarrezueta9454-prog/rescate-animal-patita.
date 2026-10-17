# Sistema de Control de Rescate y Adopción Animal (PatitasApp)

Actividad #1 · Desarrollo de Sistemas Informáticos · Universidad Técnica de Manabí

Sistema para gestionar casos de rescate en un refugio animal (perros, gatos y fauna silvestre):
reporte de rescates, asignación de voluntarios/veterinarios y control de estados del caso.

## Patrones de diseño aplicados

| Patrón | Dónde | Para qué |
|---|---|---|
| Singleton | `GestorCasos`, `ConexionDB` | Una única instancia del motor de casos y de la conexión a datos |
| Observer | `Sujeto`, `Observador`, usuarios | Notificar automáticamente a voluntarios y veterinarios ante nuevos rescates |
| Factory Method | `ExpedienteFactory` y subclases | Crear expedientes distintos según la especie |
| MVC | `model/`, `view/`, `controller/` | Separar lógica de negocio, interfaz y control |

## Estructura

```text
src/
├── model/        animal.py, caso.py, estado.py, usuario.py
├── patterns/     singleton/, observer/, factory/
├── controller/   caso_controller.py
├── view/         caso_view.py
└── main.py
tests/            test_sistema.py
docs/             diagramas y capturas
```

## Ejecutar

```bash
cd src
python main.py
```

Pruebas:

```bash
python -m unittest discover -s tests
```

## Flujo de trabajo (Gitflow)

- `master`: versiones estables (tag `v1.0.0`)
- `develop`: integración
- `feature/*`: una rama por funcionalidad o patrón
- `release/*`: preparación de versiones
