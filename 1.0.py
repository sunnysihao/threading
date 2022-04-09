# -*- coding = utf-8 -*-
import threading
import time
import spider


def single_thread():
    print("spider_begin")
    for url in spider.urls:
        spider.craw(url)
    print("spider_end")

def multi_thread():
    print("spider_begin")
    threads = []
    for url in spider.urls:
        threads.append(
            threading.Thread(target=spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("spider_end")

if __name__=='__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("单线程消耗时间：", end - start, "秒")

    start = time.time()
    multi_thread()
    end = time.time()
    print("多线程消耗时间：", end - start, "秒")
