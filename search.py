from ddgs import DDGS


print("Welcome to the WebLite CLI Tool")

def validate():
    while True:
        try:
            max_results = input("Enter the number of results: ")
            max_results = int(max_results)  # Attempt to convert to integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Continue to the next iteration of the loop
        
        if max_results < 0:
            print("max_results cannot be negative. Please enter a positive number.")
            continue  # Continue to the next iteration of the loop
        else:
            break

    return max_results

def search_ddgs_text():
    region='us-en'
    query = input("Enter your search: ")
    max_results = validate()
    results = DDGS().text(query=query, region=region, max_results=int(max_results))
    print("Searching DuckDuckGo for:", query)
    for r in results:
        print(f"Title: {r['title']}")
        print(f"URL: {r['href']}")
        print(f"Snippet: {r['body']}\n")

def search_ddgs_images():
    query = input("Enter your search: ")
    max_results = input("Enter the number of results: ")
    results = DDGS().images(query, max_results=int(max_results))
    for r in results:
        print(f"Title: {r['title']}")
        print(f"Image: {r['image']}")
        print(f"Thumbnail: {r['thumbnail']}")
        print(f"URL: {r['url']}\n")

def search_ddgs_videos():
    query = input("Enter your search: ")
    max_results = input("Enter the number of results: ")
    results = DDGS().videos(query, max_results=int(max_results))
    for r in results:
        print(f"Title: {r['title']}")
        print(f"Url: {r['content']}")
        print(f"Description: {r['description']}")
        print(f"Length: {r['duration']}")
        print(f"Published: {r['published']}")
        print(f"Publisher: {r['publisher']}")
        print(f"ViewCount: {r['statistics']['viewCount']}")
        print(f"Uploader: {r['uploader']}\n")

search_ddgs_text()

# search_ddgs_images()
# search_ddgs_videos()