import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    #to get the response and we need to provide url from where we need to get the response
    response = requests.get(url) 
    data = response.json()
    print(data)

fetch_random_user()
