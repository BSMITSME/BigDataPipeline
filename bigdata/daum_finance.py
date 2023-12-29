import requests
import urllib.request as req
from bs4 import BeautifulSoup
import json 
url = "https://m.finance.daum.net/myfeed"
res = requests.get(url)
# res = req.urlopen(url).read()
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
# #soup = BeautifulSoup(res, 'html.parser')
upstream = soup.select_one('#root > div > main > section > article:nth-child(4) > div.ranking.kosdaq > ul > li:nth-child(1) > a > p.rAlign > span')
# print(upstream)