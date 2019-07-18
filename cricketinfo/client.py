import requests
pk = input("Enter pk:")
url = "http://localhost:8000/api/country/%s"%pk
resp = requests.get(url)
print(resp)
print(resp.json())