from modules.hosts import obtener_hosts
from modules.reports import generar_csv
from modules.alerts import obtener_alertas
from modules.pdf_report import generar_pdf

print("================================")
print(" Monitorización Zabbix")
print("================================")

hosts = obtener_hosts()

activos = 0
caidos = 0

print("\nHosts monitorizados:\n")

for host in hosts:

    print(f"{host['nombre']} - {host['estado']}")

    if host["estado"] == "Activo":
        activos += 1
    else:
        caidos += 1

print("\n================================")
print(" RESUMEN")
print("================================\n")

print(f"Hosts totales: {len(hosts)}")
print(f"Hosts activos: {activos}")
print(f"Hosts caídos: {caidos}")

if caidos > 0:
    print("Estado general: ATENCIÓN")
else:
    print("Estado general: CORRECTO")


alertas = obtener_alertas()

alertas_altas = 0
alertas_medias = 0
alertas_bajas = 0

for alerta in alertas:

    if alerta["criticidad"] == "Alta":
        alertas_altas += 1

    elif alerta["criticidad"] == "Media":
        alertas_medias += 1

    elif alerta["criticidad"] == "Baja":
        alertas_bajas += 1

print("\n================================")
print(" ALERTAS ACTIVAS")
print("================================\n")

for alerta in alertas:

    print(
        f"[{alerta['criticidad'].upper()}] "
        f"{alerta['host']}"
    )

    print(alerta["problema"])
    print()

print("================================")
print(" ESTADÍSTICAS DE ALERTAS")
print("================================\n")

print(f"Alertas altas: {alertas_altas}")
print(f"Alertas medias: {alertas_medias}")
print(f"Alertas bajas: {alertas_bajas}")

print("\n================================")
print(" INFORMES GENERADOS")
print("================================\n")

# Fuera del for
generar_csv(hosts, alertas)
generar_pdf(hosts, alertas, activos, caidos, alertas_altas, alertas_medias, alertas_bajas)