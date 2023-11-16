from zeep import Client
from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


headers = {
    'x-client-id': '65265ed612e5356e23ce69ad',
    'x-app-id': '65265ed612e5356e23ce69af',
}

# Set the GraphQL query
query = """
      query {
    vehicleList(page: 0, size: 8) {
      id
      naming {
        make
        model
        chargetrip_version
      }
      media {
        image {
          thumbnail_url
        }
      }
      range {
          chargetrip_range {
              best
              worst
              }

          }
      connectors{
          time
          }
      }
    }
     """

# Set the variables for the query
variables = {
    'page': 1,
    'size': 10,
    'search': 'example',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result=None
    data=None
    naming_string=[]
    coordonnees = {"lat": 45.86298, "lng": 5.95301}
    if request.method == 'POST':
        num1 = int(request.form['vitesse'])
        num2 = int(request.form['distance'])
        num3 = int(request.form['tempcharg'])
        client = Client('http://127.0.0.1:8000/?wsdl')
        result=client.service.calcultrajetcharg(num1, num2, num3)
        print(result)
        
    response = requests.post("https://api.chargetrip.io/graphql", headers=headers, json={"query": query})
    #data = {'data': {'vehicleList': [{'id': '646ca73f3f6beb1fcbdbdf70', 'naming': {'make': 'Abarth', 'model': '500e', 'chargetrip_version': 'Convertible'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/646cad69aaf5a9205eafdd1a-e09bde673cfb63561b9f0e35a2be489f30839a3e.png'}}, 'range': {'chargetrip_range': {'best': 242, 'worst': 207}}, 'connectors': [{'time': 255}, {'time': 25}]}, {'id': '646ca7235452611fc99432b0', 'naming': {'make': 'Abarth', 'model': '500e', 'chargetrip_version': 'Hatchback'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/646cad57090bbf205ced291b-188880bbb3365522700ed0b30bcabd14e9aa825b.png'}}, 'range': {'chargetrip_range': {'best': 238, 'worst': 204}}, 'connectors': [{'time': 255}, {'time': 25}]}, {'id': '638157687592b0f2c57fc08f', 'naming': {'make': 'Abarth', 'model': '500e', 'chargetrip_version': 'Scorpionissima'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/6385be4b150257d93e72d848-f0e2178714a873acb2f18d8301694359e3b53ab1.png'}}, 'range': {'chargetrip_range': {'best': 208, 'worst': 179}}, 'connectors': [{'time': 255}, {'time': 25}]}, {'id': '5f043da2bc262f1627fc0333', 'naming': {'make': 'Aiways', 'model': 'U5', 'chargetrip_version': '63 kWh (2020 - 2022)'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/642d1f78b401be28fae31ff4-b23533754d1063ca7c975f9edaf6b3265f2e4b33.png'}}, 'range': {'chargetrip_range': {'best': 354, 'worst': 304}}, 'connectors': [{'time': 645}, {'time': 34}]}, {'id': '6261f0371b50697eb77bf4cd', 'naming': {'make': 'Aiways', 'model': 'U5', 'chargetrip_version': '63 kWh (early 2022)'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/627492cbbf2e2c73dbc9bf72-052a1ecdf9acd75a9644a3737630bb9196c10585.png'}}, 'range': {'chargetrip_range': {'best': 354, 'worst': 304}}, 'connectors': [{'time': 390}, {'time': 34}]}, {'id': '635332c66aa59107aeace234', 'naming': {'make': 'Aiways', 'model': 'U6', 'chargetrip_version': '63 kWh'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/63d93846baca136bd3582486-fad61a614ce2f6087cb83650e516097813bc8bf6.png'}}, 'range': {'chargetrip_range': {'best': 367, 'worst': 315}}, 'connectors': [{'time': 390}, {'time': 34}]}, {'id': '6454c68da1f0fa1f0c5b6a17', 'naming': {'make': 'Alfa Romeo', 'model': 'Tonale', 'chargetrip_version': '1.3T Plug-In Hybrid Q4 '}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/645d368ac4654ce2d6e7f0cc-f116632b2a41b7a18a84c934afca9d5c5eacbc25.png'}}, 'range': {'chargetrip_range': {'best': 59, 'worst': 51}}, 'connectors': [{'time': 120}]}, {'id': '63b4174d179de8267cf6d6e3', 'naming': {'make': 'Audi', 'model': 'A3 Sportback', 'chargetrip_version': '40 TFSI e'}, 'media': {'image': {'thumbnail_url': 'https://cars.chargetrip.io/63bd20e48c96922417998c4e-983f314abfa1b2db2f2bd450c94cd35f6e26ec40.png'}}, 'range': {'chargetrip_range': {'best': 65, 'worst': 56}}, 'connectors': [{'time': 210}]}]}}
    if response.status_code == 200:
        data = response.json()
        vehicles = data["data"]["vehicleList"]
        namingList = []
        for vehicle in vehicles :
          info = {'marque':vehicle["naming"]["make"]}
          info.update({'modele':vehicle["naming"]["model"]})
          info.update({'VersionRechargement':vehicle["naming"]["chargetrip_version"]})
          info.update({'ImageDuVehicule' : vehicle["media"]["image"]["thumbnail_url"]})
          info.update({'AutonomieMax' :vehicle["range"]["chargetrip_range"]["best"]})
          info.update({'AutonomieMin' :vehicle["range"]["chargetrip_range"]["worst"]})
          info.update({'time' :vehicle["connectors"][0]["time"]})
          try:
              info.update({'time2' :vehicle["connectors"][1]["time"]})
          except IndexError:
              info.update({'time2' :None})
          namingList.append(info)
    else:
         print(f"Erreur: {response.status_code} - {response.text}")
         return namingList
        
    return render_template('index.html', result=result, data=data, coordonnees=coordonnees, namingList=namingList)
    
  
if __name__ == '__main__':
    app.run(debug=True)

