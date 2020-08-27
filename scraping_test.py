import sqlite3 
from bs4 import BeautifulSoup
import requests
#---------------------------------
#insertdb
#link      アンカーにURL 
#sentence  アンカー文書
#-------------------------------

def insert(link,sentence):
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    c = conn.cursor()
    sql = 'INSERT INTO linkdb(link,sentence) VALUES(?,?)'
    data = (link,sentence)
    c.execute(sql, data)
    conn.commit()
    conn.close()


url = "https://www.sanfrecce.co.jp/clubs/top_players"
r = requests.get(url)
soup = BeautifulSoup(r.text)

titles =soup.select("a")
print(titles)
for title in titles:
  link = title.get("href")
  urlstr=title.text
  print("LINK=",link)
  print("Text=",urlstr)
  insert(link,urlstr)
