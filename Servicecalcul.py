from spyne import Application, rpc, ServiceBase, Unicode, Integer, Iterable, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import math
import requests

class CalculTraj(ServiceBase):
 
 @rpc(Integer, Integer, Integer, _returns=Unicode)        
 def calcultrajetcharg(ctx, vitesse, distance, tempscharg):
     heure=distance/vitesse
     print(f"Heure calculée : {heure}")
     minu=heure % 1
     minu=minu*60 
     minu=int(minu)
     minu = minu + tempscharg
     
     heure=math.trunc(heure)
     print(f"Heure après trunc : {heure}")
     heure= int(heure)
     print(f"Heure après int : {heure}")
     
     print(f"heure : {heure}h{minu}min")
     if ( minu >= 60 & heure >= 1):
         heure= heure+1
         minu= minu-60    
         return f"Le temps de trajet avec le chargement est de {heure}h{minu}min"
 
     if (heure < 1 ):
         
         return f"Le temps de trajet avec le chargement est de {minu}min"
     
 def ListeBorne(ServiceBase):
     
        url = "https://api.openchargemap.io/v3/poi/?output=json&countrycode=FR&maxresults=1000"
        response = requests.get(url)
        
        # The data is returned as a JSON object, so we can convert it to a Python dictionary
        data = response.json()
        
        # Now you can work with the data. For example, to print the address info of each charging station:
        for station in data:
            print(station['AddressInfo'])
     
application = Application(
    [CalculTraj], 
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
    )
 
wsgi_application = WsgiApplication(application)
 
server = make_server('127.0.0.1', 8000, wsgi_application) 
server.serve_forever()



