import csv


def generar_csv(hosts, alertas):

    with open(
        "reports/informe_completo.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(
            [
                "Tipo",
                "Host",
                "Estado",
                "Problema",
                "Criticidad"
            ]
        )

        for host in hosts:

            escritor.writerow(
                [
                    "HOST",
                    host["nombre"],
                    host["estado"],
                    "",
                    ""
                ]
            )

        for alerta in alertas:

            escritor.writerow(
                [
                    "ALERTA",
                    alerta["host"],
                    "",
                    alerta["problema"],
                    alerta["criticidad"]
                ]
            )

    print("Informe completo generado correctamente")