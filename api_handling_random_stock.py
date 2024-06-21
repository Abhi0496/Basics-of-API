import requests

def random_stock():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"

    response = requests.get(url)

    data = response.json()

    if data["success"] and "data" in data:
        name = data["data"]["Name"]
        symbol = data["data"]["Symbol"]
        current_price = data["data"]["CurrentPrice"]
        return name,symbol,current_price
    else:
        raise Exception("Data not available")

def main():
    try:
        name,symbol,current_price = random_stock()
        print(f"Name: {name} \nSymbol: {symbol} \nCurrent Price: {current_price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
