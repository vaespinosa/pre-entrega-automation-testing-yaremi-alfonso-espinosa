# Pre-Entrega Automation Testing

Este proyecto automatiza pruebas funcionales sobre el sitio https://www.saucedemo.com usando Selenium WebDriver y Pytest.

## Estructura de carpetas

- `tests/`: Pruebas automatizadas (Pytest)
- `utils/`: Funciones auxiliares y utilidades
- `datos/`: Datos externos (CSV/JSON) si aplica
- `reports/`: Reportes HTML y capturas de pantalla

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Git & GitHub

## Instalación de dependencias

1. Instala Python 3.8+
2. Instala las dependencias:
   ```bash
   pip install selenium pytest pytest-html
   ```

## Ejecución de pruebas

Ejecuta los tests y genera el reporte HTML:
```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

## Evidencias
- Capturas automáticas en caso de fallo
- Reporte HTML en `reports/`

## Propósito
Automatizar y validar los flujos principales de login, navegación de catálogo y carrito en saucedemo.com para prácticas de testing.

## Repositorio
Sube este proyecto a GitHub con el nombre:
`pre-entrega-automation-testing-[nombre-apellido]`

## Commits
Realiza commits frecuentes y descriptivos mostrando el avance.
