from time import time
import multiprocessing


def f(a):
    result = a
    for x in range(10000):
        for y in range(10000):
            result = result + x * y
    print(result)
    return result


if __name__ == "__main__":
    a = 1
    start = time()
    p1 = multiprocessing.Process(target=f, args=(a,))
    p1.start()
    print(str(time() - start))
