from spider.baike_spider import url_manager, html_downloader, html_parser,html_outputer
import requests
from lxml import etree
import threading
import time

class SpiderMain(object):
    #初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.root_url = "http://book.qidian.com/info/63856"
        #直到最后一个线程才打印
        self.count = 0
    #sum为爬取成功页面，basescore为最低分，basewordcount为最少字数,basewordclick为最少点击
    def craw(self, sum = 5, basescore = 8, basewordcount = 50, basewordclick = 50):
        count = 1
        sumcount=1
        temp = 1;
        self.urls.add_new_url('http://r.qidian.com/?chn=21')
        self.urls.add_new_url(self.root_url)
        #下面四行传递一个比较参数，"万总点击"，用于和"总点击"区分
        url = "http://book.qidian.com/info/63856"
        html_cont = requests.get(url)
        selector = etree.HTML(html_cont.text)
        word_click_back = selector.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/p[3]/cite[2]/text()')
        while self.urls.has_new_url():
            try:
                #从URL管理器取出URL
                new_url = self.urls.get_new_url()

                #输出当前爬取进度
                print('craw %d : %s ;success :%d ' % (sumcount, new_url, count))
                #网页下载器获取HTML页面
                html_cont2 = self.downloader.download(new_url)
                #错误处理
                if html_cont2 is None:
                    sumcount += 1
                    continue
                #网页解析器获取数据和URL
                new_urls, new_data = self.parser.parse(new_url, html_cont2.text, word_click_back[0])
                #将URL添加进URL管理器
                self.urls.add_new_urls(new_urls)
                #将数据存放在output中
                if new_data is not None:
                   temp = self.outputer.collect_data(new_data, count, basescore, basewordcount, basewordclick)
                # 错误处理
                if temp is None:
                    sumcount += 1
                    continue
                count = temp
                if count > sum:
                    break
                sumcount += 1
                time.sleep(1)
            except():
                print('craw failed')
        if self.count > 40:
            self.outputer.output_html()
        else:
            self.count = self.count + 1


if __name__=="__main__":
    # root_url="http://baike.baidu.com/item/Python"

    obj_spider = SpiderMain()
    i = 0
    n = 100
    threads = []
    while i < n:
        threads.append(threading.Thread(target=obj_spider.craw, name='LoopThread'+str(i)))
        i = i+1
    for t in threads:
        t.start()

