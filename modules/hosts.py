def obtener_hosts():

    hosts = [
        {
            "nombre": "Servidor-Web01",
            "estado": "Activo",
            "ip": "192.168.1.10",
            "so": "Windows Server 2022"
        },
        {
            "nombre": "Servidor-DB01",
            "estado": "Activo",
            "ip": "192.168.1.20",
            "so": "Ubuntu Server 24.04"
        },
        {
            "nombre": "Firewall01",
            "estado": "Activo",
            "ip": "192.168.1.1",
            "so": "pfSense"
        },
        {
            "nombre": "Switch-Core01",
            "estado": "Caído",
            "ip": "192.168.1.254",
            "so": "Cisco IOS"
        }
    ]

    return hosts