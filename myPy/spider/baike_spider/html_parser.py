from bs4  import BeautifulSoup
import re
import urllib.parse
import requests
from lxml import etree
class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"//book.qidian.com/info/\d+"))
        for link in links:
            new_url = link['href'] 
            #按照page_url来补全new_url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)  
        return new_urls




    def _get_score_url(self,page_url):
        #"http://book.qidian.com/info/1004608738"
        #http://book.qidian.com/ajax/comment/index?_csrfToken=hRMAi3nDUU6l7ZJo3hOcTeqXlFOcgJI8ZzGepfcq&bookId=20117
        url=None
        try:
            url = "http://book.qidian.com/ajax/comment/index?_csrfToken=T8iboC6s6L9XdF1szej0nl7Aoe7Emw8uFPKUw68A&bookId="
            id = re.search('info/(\d+)', page_url, re.S).group(1)
            url = url+id
        except:  
            return None  
        return url
    
    def _get_new_data(self, page_url, word_click_back):
        try:
            res_data = {}
            score = 0
            res_data['url'] = page_url
            #获取getURL，获取预加载数据
            score_url = self._get_score_url(page_url)
            res_data['score'] = 0

            if score_url is not None:
                        score_cont = requests.get(score_url)
                        try:
                           score = re.search('rate":(.*?),', score_cont.text, re.S).group(1)
                        except:
                            score = 0


            res_data['score'] = score

            # 以下使用Xpath
            html_cont = requests.get(page_url)
            selector = etree.HTML(html_cont.text)

            title_node = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/h1/em')
            res_data['title'] = title_node[0].text

            # 小说简介
            summary_node = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[2]')
            res_data['summary'] = summary_node[0].text
            #获取字数信息


            word_count = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/em[1]/text()')
            res_data['word_count'] = word_count[0]
            #获取"万总点击",将值赋给res_data['word_click_num']
            word_click_back1 = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/cite[2]/text()')
            word_click_num1 = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/em[2]/text()')
            if word_click_back1[0] == word_click_back:
                res_data['word_click_num'] = word_click_num1[0]
            else:
                res_data['word_click_num'] = None

             #获取小说类别
            book_category = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[1]/a[1]/text()')
            res_data['book_category'] = book_category[0]
        except:
            return None
        return res_data
             
    
    def parse(self, page_url, html_cont, word_click_back):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, word_click_back)
        return new_urls, new_data
    
    



