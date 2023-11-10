from flask import Flask, render_template, request, jsonify
from werkzeug.urls import url_encode
from pysnmp.hlapi import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@10.0.0.4:5434/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    nom_machine = db.Column(db.String(200), nullable=False)
    ip_address = db.Column(db.String(50), nullable=False)
    monitoring_interval = db.Column(db.String(200), nullable=True)

class Oid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oid_value = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

def fetch_snmp_data(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        return str(errorIndication)
    elif errorStatus:
        return str('%s at %s' % (errorStatus.prettyPrint(),
                                 errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            return ' = '.join([x.prettyPrint() for x in varBind])

@app.route('/', methods=['GET'])
def index():
    results = []
    hosts = Device.query.all()
    print(hosts)
    oids = Oid.query.all()

    return render_template('index.html', results=results, hosts=hosts, oids=oids)

@app.route('/snmp_request', methods=['POST'])
def snmp_request():
    results = []
    hosts = Device.query.all()
    oids = Oid.query.all()

    host = request.form.get('host', '10.0.0.4')
    oid_value = request.form.get('oid', '1.3.6.1.2.1.1.1.0')
    community = 'public'

    if not host or not oid_value:
        return "Host or OID missing!", 400

    result = fetch_snmp_data(host, community, oid_value)
    results.append(result)

    return render_template('index.html', results=results, hosts=hosts, oids=oids)

@app.route('/add_machine', methods=['POST'])
def add_machine():
    results = []
    hosts = Device.query.all()
    oids = Oid.query.all()

    host = request.form.get('host', '10.0.0.4')
    description = request.form.get('description')
    nom_machine = request.form.get('nom_machine')
    monitoring_interval = request.form.get('monitoring_interval')

    new_device = Device(
            description=description,
            nom_machine=nom_machine,
            ip_address=host,
            monitoring_interval=monitoring_interval,
        )


    try:
        db.session.add(new_device)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Database error: {e}")
        return str(e), 500

    return render_template('index.html', results=results, hosts=hosts, oids=oids)


@app.route('/delete_machine', methods=['POST'])
def delete_machine():
    results = []
    hosts = Device.query.all()
    oids = Oid.query.all()

    machine_to_delete = request.form.get('machine_to_delete')

    if not machine_to_delete:
        return "Nom de la machine à supprimer manquant!", 400

    # Recherchez l'entrée dans la table Device par nom de machine
    device_to_delete = Device.query.filter_by(nom_machine=machine_to_delete).first()

    if not device_to_delete:
        return f"Aucune entrée trouvée pour la machine {machine_to_delete}", 404

    try:
        db.session.delete(device_to_delete)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de la suppression de l'entrée : {e}")
        return str(e), 500
    return render_template('index.html', results=results, hosts=hosts, oids=oids)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
