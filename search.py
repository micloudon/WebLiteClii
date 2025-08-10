from ddgs import DDGS

print("Welcome to the WebLite CLI Tool")

def search_ddgs_text():
    region='wt-wt'
    query = input("Enter your search: ")
    max_results = input("Enter the number of results: ")
    results = DDGS().text(query=query, region=region, max_results=int(max_results))
    print("Searching DuckDuckGo for:", query)
    for r in results:
        print(f"Title: {r['title']}")
        print(f"URL: {r['href']}")
        print(f"Snippet: {r['body']}\n")

def search_ddgs_images():
    query = input("Enter your search: ")
    max_results = input("Enter the number of results: ")
    results = DDGS().images(query, max_results=max_results)
    for r in results:
        print(f"Title: {r['title']}")
        print(f"Image: {r['image']}")
        print(f"Thumbnail: {r['thumbnail']}")
        print(f"URL: {r['url']}\n")


# search_ddgs_text()

search_ddgs_images()
