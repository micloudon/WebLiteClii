import requests
from bs4 import BeautifulSoup

url = 'http://www.google.com/search'
url1 = '''
http://www.google.com/search?
  start=0
  &num=10
  &q=redsox
  &lr=lang_fr
  &client=google-csbe
  &output=xml_no_dtd
  &cx=00255077836266642015:u-scht7a-8i
'''
params = {
    "start": "0",
    "num": "40",
    "as_q": "redsox",
    "as_eq": "Yankees",
    "client": "google-csbe",
    "output": "xml_no_dtd",
    "cx": "00255077836266642015:u-scht7a-8i"
}

url2 = 'https://en.wikipedia.org/wiki/Car'
request = requests.get(url1)


soup = BeautifulSoup(request.text, "html.parser")
all_links = soup.find_all('a')


print(request.url)

# for i in request:
#     if "href" in str(i):
#         print("True")