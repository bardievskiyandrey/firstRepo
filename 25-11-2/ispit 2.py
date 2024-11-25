import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.quotegarden.com/mind.html")
soup = BeautifulSoup(response.content, features="html.parser")
text_blocks = soup.find_all("p")
for text_block in text_blocks:
    print(text_block.text)