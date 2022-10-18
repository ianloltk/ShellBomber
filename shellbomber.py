import requests

URL = "http://hgd-speedtest-1.tele2.net/100GB.zip"
response = requests.get(URL)
open("getrektgoogle.zip", "wb").write(response.content)