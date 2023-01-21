from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.bbc.co.uk/"
url1 = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/chilled-soup-sandwiches-and-salad-pots/pound3.90-meal-deal?page=1"
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

webbrowser.open(url1)