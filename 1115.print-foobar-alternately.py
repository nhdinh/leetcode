# 1115. Print FooBar Alternately

import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = threading.Lock()
        self.lockFoo.acquire()
        self.lockBar = threading.Lock()

    def foo(self, printFoo):
        for i in range(self.n):
            self.lockBar.acquire()
            printFoo()
            self.lockFoo.release()


    def bar(self, printBar):
        for i in range(self.n):
            self.lockFoo.acquire()
            printBar()
            self.lockBar.release()