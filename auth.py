import os
import requests

url = "http://localhost:8080/basic-auth/russ/test"
username = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")

response = requests.get(url, auth=(username, password))
print(response.text)

