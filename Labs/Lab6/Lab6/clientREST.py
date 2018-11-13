#GET
import requests

r = requests.get(URI)
print(r.status_code)
data = r.json()
print(data)


# POST
payload = {'ids': [12, 3, 4, 5, 6] }
r = requests.post("http://httpbin.org/post", json=payload)
r = requests.post(url, data=json.dumps(payload))
print(r.text)
