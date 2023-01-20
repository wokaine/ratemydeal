from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.co.uk/"
req = requests.get(url)

#soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
soup = BeautifulSoup(req.text, 'html.parser')

head = soup.head
body = soup.body

#print(head.contents)
#print(body.contents)

for string in head.stripped_strings:
    print(string)

for string in body.stripped_strings:
    print(string)