import requests
import json
# For the purpose of this example, we use the requests library to make the HTTP request.
# You can install it using `pip install requests`.

# Set the headers with your API key
headers = {
    'x-client-id': '65265ed612e5356e23ce69ad',
    'x-app-id': '65265ed612e5356e23ce69af',
}

# Set the GraphQL query
query = '''
{
  vehicleList {
    id
    naming {
      make
      model
      version
      edition
      chargetrip_version
    }
    drivetrain {
      type
    }
    connectors {
      standard
      power
      max_electric_power
      time
      speed
    }
    adapters {
      standard
      power
      max_electric_power
      time
      speed
    }
  }
}
'''

# Set the variables for the query
variables = {
    'page': 1,
    'size': 10,
    'search': 'example',
}

# Make the HTTP POST request to the GraphQL API
response = requests.post('https://api.chargetrip.io/graphql', json={'query': query, 'variables': variables}, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Save the data to a JSON file
    with open('response.json', 'w') as file:
        json.dump(data, file)

    print('Data saved to response.json')

else:
    print(f'Request failed with status code {response.status_code}')
    print(response.text)