import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.quotegarden.com/mind.html")
soup = BeautifulSoup(response.content, features="html.parser")
text_block = soup.find_all("p")
print(text_block)