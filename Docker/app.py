from flask import Flask, render_template, request, jsonify
from werkzeug.urls import url_encode
from pysnmp.hlapi import *

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        host = request.form.get('host', '10.0.0.4')
        oid = request.form.get('oid', '1.3.6.1.2.1.1.1.0')
        community = 'public'

        print("Host:", host)
        print("OID:", oid)

        if not host or not oid:
            return "Host or OID missing!", 400

        result = fetch_snmp_data(host, community, oid)
        results.append(result)

    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)