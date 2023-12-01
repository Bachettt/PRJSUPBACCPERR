CREATE TABLE device (
    id SERIAL PRIMARY KEY,
    nom_machine VARCHAR(200) NOT NULL,
    ip_address VARCHAR(50) NOT NULL,
    description VARCHAR(200),
    monitoring_interval VARCHAR(200)
);

CREATE TABLE Logs (
    id SERIAL PRIMARY KEY,
    temps VARCHAR(255) NOT NULL,
    nom_machine VARCHAR(255) NOT NULL,
    oid_value VARCHAR(255) NOT NULL,
    val_text VARCHAR(255),
    val_num BIGINT
);

CREATE TABLE oid (
    id SERIAL PRIMARY KEY,
    description VARCHAR(200) NOT NULL,
    oid_value VARCHAR(200) NOT NULL
);

INSERT INTO device (nom_machine, ip_address, description, monitoring_interval)
VALUES ('DOCKER_LIN', '10.0.0.4', 'Machine contenant docker', '5'), ('Windows-Client-Serv', '10.0.0.5', 'Machine windows', '5'), ('MACHINE-SCRIPT-CLIENT', '10.0.0.6', 'Machine q
ui lance les scripts snmp','5');

INSERT INTO oid (description, oid_value)
VALUES ('sysDescr', '1.3.6.1.2.1.1.1.0'), ('sysUpTime', '1.3.6.1.2.1.1.3.0'), ('ifNumber', '1.3.6.1.2.1.2.1.0');