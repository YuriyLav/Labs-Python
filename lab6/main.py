import sys
import threading

counter = 0
sys.setswitchinterval(0.000001)


def process():
    global counter
    while counter < 100:
        semaphore.acquire()  # уменьшает счетчик (-1)
        print(counter)
        counter += 1
        semaphore.release()  # увеличивает счетчик (+1)


semaphore = threading.Semaphore()
threads = []
for i in range(2):
    thread = threading.Thread(target=process)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
