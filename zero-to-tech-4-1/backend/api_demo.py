import requests

resp = requests.get("https://httpbin.ceshiren.com/get")

print(resp.json())
