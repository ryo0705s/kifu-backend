import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.co.jp/b?ie=UTF8&node=8443136051")

soup = BeautifulSoup(response.text, "html.parser")

for element in soup.find_all("a", text=True):
  print(element.getText())