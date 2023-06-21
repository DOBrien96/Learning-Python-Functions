import requests
import config

url = "address of the GET request for the api (URL)"


headers = {
    "Authorization": "Bearer " + config.api_key
} #The api needs to authenticate who you are to allow access.

params = {
    "term": "Barber", #Filtering, asking api to find barbers.
    "loaction": "NYC" #Filtering, picking from this location.
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"] #Puts businesses into a dictionary

name = [business["name"]#The "name" fetches all barber names
        for business in businesses if business["rating"] > 4.5]
#Using a list comprehension to find all barbers with a rating over 4.5

for business in businesses: #Iterating over all the businesses in NYC
    print(business["name"])