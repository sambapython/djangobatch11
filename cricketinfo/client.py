import requests
url = "http://localhost:8000/api/country"
resp = requests.get(url)
print(resp)
print(resp.json())