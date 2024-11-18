import requests
from bs4 import BeautifulSoup
response = requests.get("http://books.toscrape.com")
soup = BeautifulSoup(response.text, features="html.parser")
book_name = soup.find_all("h3")
book_price = soup.find_all("p", {"class":"price_color"})
for i in range(0, len(book_name)):
    print(f"{book_name[i].text} {book_price[i].text}")