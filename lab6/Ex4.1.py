import requests
from time import time
import threading
from urllib import request

sites = [
    "https://www.apple.com/",
    "https://www.google.ru/",
    "https://yandex.ru/",
    "https://vk.com/",
    "https://www.instagram.com/",
    "https://mail.google.com/",
    "https://www.hp.com/",
    "https://ru.wikipedia.org/",
    "https://www.youtube.com/",
    "https://www.microsoft.com/"
]


def get_sites():
    for site in sites:
        requests.get(site)


start = time()
t1 = threading.Thread(target=get_sites)
t1.start()
t1.join()
print("With 1 thread: " + str(time() - start) + " seconds")

start1 = time()
t2 = threading.Thread(target=get_sites)
t2.start()
t3 = threading.Thread(target=get_sites)
t3.start()
t2.join()
t3.join()
print("2 threads: " + str(time() - start1) + " seconds")
