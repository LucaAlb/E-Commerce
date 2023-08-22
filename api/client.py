import requests


api_url = "http://localhost:8000/api"
response = requests.get(api_url, params={"dipartimento": "magazzino"})

if response.status_code == 200:
    data = response.json()
    # message = data['message']
    print(data)
else:
    print('Error:', response.status_code)



