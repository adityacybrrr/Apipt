import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python POST",
    "body": "Testing POST via script",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

