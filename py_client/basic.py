import requests


endpoint = 'https://httpbin.org/anything'

requests_sl = requests.get(endpoint, data={'client': 'server','client2': 'server2'})
print(requests_sl.text)
print(requests_sl.json())
