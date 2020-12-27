import urllib.request
import time
import threading
def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()
def read(q):
    with lock:
        with urllib.request.urlopen(q) as u:
            return u.read()

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org'
]
start = time.time()
lock = threading.Lock()
for url in urls:
    read_url(url)
print(time.time() - start)
start1=time.time()
threads = [threading.Thread(target=read_url, args=(url,)) for url in urls]
for i in threads:
    i.start()
for i in threads:
    i.join()
t=time.time()
print(t-start1)
