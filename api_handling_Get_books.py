import requests

def get_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"

    response = requests.get(url)

    data = response.json()

    if data["statusCode"] == 200 and "data" in data:
        author = data["data"]["volumeInfo"]["authors"][0]
        title = data["data"]["volumeInfo"]["title"]
        #print(author)
        #print(title)

#get_books()
        return title, author
    else:
        raise Exception("Failed to fetch the details")



def main():
    try:
        title,author = get_books()
        print(f"Title: {title} \nAuthor: {author}")
    except Exception as e:
        print(str(e))

    pass

if __name__ == "__main__":
    main()
