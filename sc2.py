import requests
url = "https://chart.yahoo.co.jp/?code=6758.T&tm=1d&size=e&vip=off"
file_name = "sony.jpg"
response = requests.get(url)
image = response.content
with open(file_name, "wb") as img:
    img.write(image)
print("OK")