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


def get_sites(a, b):
    for i in range(a, b):
        requests.get(sites[i])


start = time()
p1 = threading.Thread(target=get_sites, args=(0, 10))
p1.start()
p1.join()
print("With 1 thread: " + str(time() - start) + " seconds")

n = 10
threads = []
x = 0
y = 1
start1 = time()
for k in range(n):
    thread = threading.Thread(target=get_sites, args=(x, y))
    thread.start()
    threads.append(thread)
    x += 1
    y += 1
for thread in threads:
    thread.join()
print(str(n) + " threads: " + str(time() - start1) + " seconds")
