import requests
import json

url = "https://jsonplaceholder.cypress.io/posts"

payload1 = {}
headers1 = {}

response1 = requests.request("GET", url, headers=headers1, data=payload1)

print(response1.text)

payload2 = json.dumps({
  "title": "recommendation",
  "body": "motorcycle",
  "userId": 12
})
headers2 = {
  'Content-Type': 'application/json'
}

response2 = requests.request("POST", url, headers=headers2, data=payload2)

print(response2.text)