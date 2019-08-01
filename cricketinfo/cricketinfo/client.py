import requests
resp = requests.get('http://localhost:8000/api/country/',
	headers={"Authorization":"Token a10b80094e7195e8f05dd7b8940381dc11d7a210"})
print(resp)