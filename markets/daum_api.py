import bs4
from bs4 import BeautifulSoup as bs
import os
import sys
import urllib.request
client_id = "eunxfnjVQmugrB6ZIXlh"
client_secret = "mkrvDvbiYY"
encText = urllib.parse.quote("US election 2020 polls")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#url = 'http://finance.daum.net/api/market_index/days?page=1&perPage=100&market=KOSPI&pagination=true'
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
