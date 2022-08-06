import threading
from random import randint
from time import time
from multiprocessing import Process
from threading import Thread

N = 5000


def new_element(qj, pi):
    return 1 / (1 + abs(qj - pi))


def create_matrix(q, p, a, b):
    matrix = []
    for i in range(a, b):
        row = []
        for j in range(a, b):
            row.append(new_element(q[j], p[i]))
        matrix.append(row)


Q = []
P = []

for k in range(0, N):
    Q.append(randint(-10, 10))
    P.append(randint(-10, 10))

start = time()
create_matrix(Q, P, 0, N)
print("One thread: " + str(time() - start))

threads = []
n = 5
x = 0
y = 1000

start1 = time()
for k in range(n):
    thread = threading.Thread(target=create_matrix, args=(Q, P, x, y))
    thread.start()
    threads.append(thread)
    x += 1000
    y += 1000
for thread in threads:
    thread.join()

print(str(n)+" threads: " + str(time() - start1))
