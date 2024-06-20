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

def main():
    #its better to do try catch in case of web requests to avoid crashing of main
    try:
        username, country = fetch_random_user()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
