import requests
class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return
        response = requests.get(url, timeout=2)
         
        if response.status_code != 200:
            return None
         
        return response
    
    



