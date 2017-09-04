import threading


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.lock = threading.Lock()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        
    def add_new_urls(self, urls):
        self.lock.acquire()
        if urls is None or len(urls) == 0:
            self.lock.release()
            return
        for url in urls:
            self.add_new_url(url)
        self.lock.release()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        self.lock.acquire()
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        self.lock.release()
        return new_url


    
    
        
    
    
    
    
    
    

    
   
    
    
    
    



