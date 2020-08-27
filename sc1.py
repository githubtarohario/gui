import requests
r=requests.get('https://www.yahoo.co.jp')
print(r.text)
print("encoding",r.encoding)
