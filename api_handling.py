import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    #to get the response and we need to provide url from where we need to get the response
    response = requests.get(url) 

    #to get data in JSON format
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user details")

fetch_random_user()
