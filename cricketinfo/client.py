import requests
resp = requests.get('http://localhost:8000/api/country/',
	headers={"Authorization":"Token a2eaa1a2baf5ac606db791470dc4a5f2f1af4593"})
print(resp)