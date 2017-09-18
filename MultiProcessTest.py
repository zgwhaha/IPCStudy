from concurrent.futures import ThreadPoolExecutor
import time


def return_future(msg):
    time.sleep(3)
    return msg


# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2100)

# 往线程池加入2个task
def threadtest1(m):
    for i in range(10):
        time.sleep(1)
        print(i+m)
f1 = pool.submit(threadtest1, 0)
f2 = pool.submit(threadtest1,100)

print(f1.done())
print(f2.done())
time.sleep(3)

print(f1.result())
print(f2.result())
print(f1.done())
time.sleep(3)
print(f2.done())