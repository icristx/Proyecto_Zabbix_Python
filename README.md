# Proyecto Zabbix Python

## Descripción

Aplicación desarrollada en Python para la simulación de monitorización de infraestructuras informáticas y la generación automática de informes.

El proyecto permite gestionar hosts monitorizados, registrar alertas y generar informes en formato CSV y PDF con información detallada sobre el estado de la infraestructura.

---

## Funcionalidades

* Monitorización de hosts.
* Gestión de alertas.
* Generación de informes CSV.
* Generación de informes PDF.
* Estadísticas de disponibilidad.
* Estadísticas de alertas.
* Inventario de hosts con dirección IP y sistema operativo.
* Arquitectura modular preparada para futuras integraciones con APIs de monitorización.

---

## Tecnologías utilizadas

* Python
* ReportLab
* CSV
* Visual Studio Code

---

## Estructura del proyecto

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
├── config.py
├── main.py
└── README.md


---

## Ejecución

Ejecutar la aplicación desde la terminal:

bash
python main.py

---

## Resultados generados

La aplicación genera automáticamente:

* Informe CSV (informe_completo.csv)
* Informe PDF (informe_monitorizacion.pdf)

---

## Mejoras futuras

* Integración con la API de Zabbix.
* Generación avanzada de gráficos.
* Exportación de informes ampliados.
* Integración con herramientas de monitorización empresariales.
* Automatización de ejecución mediante tareas programadas.

---

## Autor

Cristina

Proyecto desarrollado como práctica de automatización y monitorización de infraestructuras mediante Python.
