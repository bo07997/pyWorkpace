#coding:utf8
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
from idlelib.IOBinding import encoding
 #"http://book.qidian.com/info/1004608738"
 #http://book.qidian.com/ajax/comment/index?_csrfToken=hRMAi3nDUU6l7ZJo3hOcTeqXlFOcgJI8ZzGepfcq&bookId=20117
url=None
url="http://book.qidian.com/ajax/comment/index?_csrfToken=hRMAi3nDUU6l7ZJo3hOcTeqXlFOcgJI8ZzGepfcq&bookId="
id=re.search('info/(\d+)', "http://book.qidian.com/info/1004788288", re.S).group(1)
url=url+id
url="http://book.qidian.com/info/1004608738"
html_cont = requests.get(url,timeout=0.5)
selector = etree.HTML(html_cont.text)
word_click_back= selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/cite[2]/text()')
wo = str(word_click_back)
print word_click_back[0]
[u'\u603b\u70b9\u51fb', u'\u4f1a\u5458\u5468\u70b9\u51fb1486']
[u'\u4e07\u603b\u70b9\u51fb', u'\u4f1a\u5458\u5468\u70b9\u51fb3.14\u4e07']

# score=re.search('rate":(.*?),', score_cont.text, re.S).group(1)

# print score