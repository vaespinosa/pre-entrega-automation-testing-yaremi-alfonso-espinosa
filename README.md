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
2. Crea y activa el entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Instala las dependencias desde el archivo requirements.txt:
   ```powershell
   pip install -r requirements.txt
   ```


## Ejecución de pruebas

Para ejecutar los tests y generar el reporte HTML:

1. Activa el entorno virtual:
   ```powershell
   .\venv\Scripts\Activate
   ```

2. Ejecuta los tests:
   ```powershell
   pytest tests/test_saucedemo.py -v --html=reports/reporte.html
   ```

3. Verifica el reporte generado en `reports/reporte.html`.

**Notas:**
- Los tests son independientes y automatizados.
- Si ocurre un fallo, se guarda una captura en `reports/assets/`.
- El entorno virtual debe estar activo para que se reconozcan las dependencias instaladas.

## Evidencias
- Capturas automáticas en caso de fallo
- Reporte HTML en `reports/`

---

### Colaboración y supervisión
Este proyecto fue co-trabajado con el apoyo de GitHub Copilot para la generación de código y estructura, bajo la supervisión y revisión constante de la autora humana (Yaremi Violeta Alfonso Espinosa), asegurando la comprensión y calidad de cada parte entregada.

## Propósito
Automatizar y validar los flujos principales de login, navegación de catálogo y carrito en saucedemo.com para prácticas de testing.

## Repositorio
Sube este proyecto a GitHub con el nombre:
`pre-entrega-automation-testing-[nombre-apellido]`

## Commits
Realiza commits frecuentes y descriptivos mostrando el avance.
