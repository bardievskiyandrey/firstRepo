import requests
from bs4 import BeautifulSoup
response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
coin_name = soup.find_all("p", {"class":"sc-65e7f566-0 iPbTJf coin-item-name"})
coin_value = soup.find_all("div", {"class":"sc-b3fc6b7-0 dzgUIj"})
coin_short_name = soup.find_all("p", {"class":"sc-65e7f566-0 byYAWx coin-item-symbol"})
for i in range(0, len(coin_name)):
    print(f"{coin_name[i].text} {coin_value[i].text} {coin_short_name[i].text}")