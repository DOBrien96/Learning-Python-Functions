import requests_package.requests as requests

response = requests.get("http://google.com")
print(response) #Program should say <Response [200]> if successful