from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from reportlab.lib import colors


def generar_pdf(hosts, alertas, activos, caidos, alertas_altas, alertas_medias, alertas_bajas):

    pdf = SimpleDocTemplate(
        "reports/informe_monitorizacion.pdf"
    )

    estilos = getSampleStyleSheet()

    contenido = []

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    # TÍTULO

    contenido.append(
        Paragraph(
            "Informe de Monitorización",
            estilos["Title"]
        )
    )

    contenido.append(
        Paragraph(
            f"Fecha del informe: {fecha}",
            estilos["BodyText"]
        )
    )

    contenido.append(Spacer(1, 20))

    # RESUMEN

    contenido.append(
        Paragraph(
            "Resumen de infraestructura",
            estilos["Heading2"]
        )
    )

    contenido.append(
        Paragraph(
            f"Hosts totales: {len(hosts)}",
            estilos["BodyText"]
        )
    )

    contenido.append(
        Paragraph(
            f"Hosts activos: {activos}",
            estilos["BodyText"]
        )
    )

    contenido.append(
        Paragraph(
            f"Hosts caídos: {caidos}",
            estilos["BodyText"]
        )
    )

    if caidos == 0:
        estado = "CORRECTO"
    elif caidos <= 2:
        estado = "ATENCIÓN !"
    else:
        estado = "CRÍTICO !!"

    contenido.append(
        Paragraph(
            f"Estado general: {estado}",
            estilos["BodyText"]
        )
    )

    contenido.append(Spacer(1, 20))

    contenido.append(
    Paragraph(
        "Estadísticas de alertas",
        estilos["Heading2"]
    )
)
    contenido.append(
        Paragraph(
            f"Alertas altas: {alertas_altas}",
            estilos["BodyText"]
        )
    )

    contenido.append(
        Paragraph(
            f"Alertas medias: {alertas_medias}",
            estilos["BodyText"]
        )
    )

    contenido.append(
        Paragraph(
            f"Alertas bajas: {alertas_bajas}",
            estilos["BodyText"]
        )
    )

    contenido.append(Spacer(1, 20))

    # HOSTS

    contenido.append(
        Paragraph(
            "Hosts monitorizados",
            estilos["Heading2"]
        )
    )

    datos_hosts = [
        ["Host", "Estado", "IP", "Sistema Operativo"]
    ]

    for host in hosts:
        datos_hosts.append(
            [
                host["nombre"],
                host["estado"],
                host["ip"],
                host["so"]
            ]
        )

    tabla_hosts = Table(datos_hosts)

    tabla_hosts.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)
        ])
    )

    contenido.append(tabla_hosts)

    contenido.append(Spacer(1, 20))

    # ALERTAS

    contenido.append(
        Paragraph(
            "Alertas activas",
            estilos["Heading2"]
        )
    )

    datos_alertas = [
        ["Criticidad", "Host", "Problema", "Fecha"]
    ]

    for alerta in alertas:

        datos_alertas.append(
            [
                alerta["criticidad"],
                alerta["host"],
                alerta["problema"],
                alerta["fecha"]
            ]
        )

    tabla_alertas = Table(datos_alertas)

    tabla_alertas.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)
        ])
    )

    contenido.append(tabla_alertas)
    
    contenido.append(Spacer(1, 30))

    contenido.append(
        Paragraph(
            "Informe generado automáticamente por el Sistema de Monitorización Python.",
            estilos["Italic"]
        )
    )

    pdf.build(contenido)

    print(
        "PDF generado correctamente"
    )