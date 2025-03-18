import requests


# CHANGE THESE TWO
TOKEN = "<YOUR_TOKEN_HERE>"
URL = "http://<ip>:8123/api/states"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(URL, headers=headers)
print(response.json())
