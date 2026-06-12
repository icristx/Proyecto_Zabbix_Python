# Proyecto Zabbix Python

## Descripción

Aplicación desarrollada en Python para la simulación de monitorización de infraestructuras informáticas y la generación automática de informes.

El proyecto permite gestionar hosts monitorizados, registrar alertas y generar informes en formato CSV y PDF con información detallada sobre el estado de la infraestructura.

Inspirado en entornos de monitorización como Zabbix, el proyecto ha sido diseñado con una arquitectura modular que facilita futuras ampliaciones e integraciones.

---

## Funcionalidades

* Monitorización de hosts.
* Gestión de alertas.
* Generación de informes CSV.
* Generación de informes PDF.
* Estadísticas de disponibilidad.
* Estadísticas de alertas.
* Inventario de hosts con dirección IP y sistema operativo.
* Registro de fechas de incidencias.
* Arquitectura modular preparada para futuras integraciones con APIs de monitorización.

---

## Tecnologías utilizadas

* Python
* ReportLab
* CSV
* Git
* GitHub
* Visual Studio Code

---

## Estructura del proyecto

```text
Proyecto_Zabbix_Python/
│
├── modules/
│   ├── alerts.py
│   ├── hosts.py
│   ├── pdf_report.py
│   ├── reports.py
│   └── zabbix_api.py
│
├── reports/
│
├── docs/
│
├── config.py
├── main.py
├── README.md
└── requirements.txt
```

---

## Ejecución

Ejecutar la aplicación desde la terminal:

```bash
python main.py
```

---

## Resultados generados

La aplicación genera automáticamente:

* Informe CSV (`informe_completo.csv`)
* Informe PDF (`informe_monitorizacion.pdf`)

Los informes incluyen:

* Resumen de infraestructura.
* Estadísticas de disponibilidad.
* Estadísticas de alertas.
* Inventario de hosts.
* Listado de alertas activas.
* Fecha de generación del informe.

---

## Ejemplo de funcionalidades

* Gestión de hosts monitorizados.
* Registro de incidencias y alertas.
* Exportación de datos a CSV.
* Generación automática de documentación PDF.
* Presentación de información mediante tablas.
* Clasificación de alertas por criticidad.

---

## Mejoras futuras

* Integración con la API de Zabbix.
* Obtención de datos en tiempo real.
* Generación de gráficos de monitorización.
* Automatización mediante tareas programadas.
* Exportación de informes avanzados.
* Integración con otras herramientas de monitorización.

---

## Autor

Cristina

Proyecto desarrollado como práctica de automatización y monitorización de infraestructuras mediante Python.
