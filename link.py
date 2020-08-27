from bs4 import BeautifulSoup
import requests

url = "https://www.google.co.jp"
r = requests.get(url)
soup = BeautifulSoup(r.text)

titles =soup.select("a")
#print(titles)
for title in titles:
  print("Text=",title.text)
  link = title.get("href")
  print("LINK=",link)