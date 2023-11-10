import psycopg2
from pysnmp.hlapi import *

# Connexion à la base de données
conn = psycopg2.connect(
    host="10.0.0.4",
    port=5434,
    database="mydatabase",
    user="user",
    password="password"
)

# Création d'un curseur pour exécuter des requêtes
cur = conn.cursor()

# Exécution d'une requête SELECT
cur.execute("SELECT * FROM device")

# Récupération des résultats
rows = cur.fetchall()

# Isolation des adresses IP commençant par "10.0."
ip_list = []
for row in rows:
    machine_ip = row[2]  # Remplace 2 par l'index approprié pour l'adresse IP dans la ligne de résultat
    if machine_ip.startswith("10.0."):
        ip_list.append(machine_ip)

# Envoi de la requête SNMP à chaque adresse IP
for ip in ip_list:
    community_string = "public"  # Remplace "public" par ta chaîne de communauté SNMP

    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community_string),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if error_indication:
        print(f"Erreur lors de la requête SNMP vers {ip}: {error_indication}")
    elif error_status:
        print(f"Erreur lors de la requête SNMP vers {ip}: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            oid_value = "1.3.6.1.2.1.1.1.0"
            resultat_snmp = var_bind.prettyPrint()  # Récupération du résultat SNMP
            # Insertion du résultat dans la table "logs"
            cur.execute("INSERT INTO logs (nom_machine, oid_value, val_text) VALUES (%s, %s, %s)", (ip, oid_value, resultat_snmp))
            conn.commit()

# Fermeture du curseur et de la connexion à la base de données
cur.close()
conn.close()
