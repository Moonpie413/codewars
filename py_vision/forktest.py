#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' multi porcesses test '

from multiprocessing import Process, Queue
import time

def write(queue):
    ' write function '
    todo = [x for x in range(10)]
    for task in todo:
        print('putting %s to queue'% str(task))
        queue.put(task)
        time.sleep(1)

def read(queue):
    ' write function '
    while True:
        print('get %s form queue' % queue.get(True))

def main():
    ' main function '
    queue = Queue()
    pw = Process(target=write, args=(queue,))
    pr = Process(target=read, args=(queue,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

if __name__ == '__main__':
    main()
