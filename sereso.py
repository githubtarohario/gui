import requests
from bs4 import BeautifulSoup

#Webページを取得して解析する
url = "https://www.cerezo.jp/teams/top/"
#<img src="https://www.cerezo.jp/wp-content/uploads/2020/01/1_takumi_NAGAISHI-1.jpg" alt="" class="heightLine-group2"></span>
soup = BeautifulSoup(requests.get(url).content,'lxml') # 特定のURLをBeautifulSoupにてlxmlパースし、soup変数に格納します
images = [] # 画像リストの配列

for link in soup.find_all("img"):          # imgタグを取得しlinkに格納
    if link.get("src").endswith(".jpg"):   # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src"))     # imagesリストに格納
        print(link.get("src"))
    elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
    	images.append(link.get("src"))     # imagesリストに格納
    	print(link.get("src"))
for target in images:                  # imagesからtargetに入れる
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納一番後ろをとる
        f.write(re.content) # .contentにて画像データとして書き込む