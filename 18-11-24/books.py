import requests
from bs4 import BeautifulSoup

for i in range(1, 51):
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    soup = BeautifulSoup(response.text, features="html.parser")
    page = soup.find("li", {"class": "current"})
    book_name = soup.find_all("h3")
    book_price = soup.find_all("p", {"class": "price_color"})
    print(f"{book_name[i].text} {book_price[i].text} {page.text}")