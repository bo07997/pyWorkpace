from spider.baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain2(object):
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def test_comprehensions(self):
        list_a = list(range(1, 11))
        result = [x * x for x in list_a if (x % 2 == 0)]

    def test_generator1(self):
        list_a = list(range(1, 100))
        result = (x * x for x in list_a if (x % 2 == 0))
        return result
        return 2

    def test_generator2(self, max1):
        n, a, b = 0, 0, 1
        x = int(max1)
        print(x)
        while n < int(x):
            yield b
            a, b = b, a + b
            n = n + 1
        return b


if __name__ == "__main__":
    # root_url="http://baike.baidu.com/item/Python"63856
    root_url = "http://book.qidian.com/info/3686510"
    obj_spider1 = SpiderMain2()
    print(obj_spider1.test_generator2(5))