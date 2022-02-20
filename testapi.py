import http.client
import json

conn = http.client.HTTPSConnection("www.thunderclient.com")

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

conn.request("GET", "/welcome", payload, headersList)
response = conn.getresponse()
result = response.read()

try:
    js = json.loads(result)
except:
    js = None

message = js["about"]
print(message)