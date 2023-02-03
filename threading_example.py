import threading
from typing import Callable

def printNumber(i):
    print(i, end="")

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lockZero = threading.Lock()
        self.lockEven = threading.Lock()
        self.lockOdd = threading.Lock()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.lockEven and self.lockOdd:
                printNumber(0)
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i % 2 == 0:
                with self.lockZero and self.lockOdd:
                    printNumber(i)
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i % 2 == 1:
                with self.lockZero and self.lockEven:
                    printNumber(i)
        
        

if __name__ == '__main__':
    ss = ZeroEvenOdd(3)
    thread1 = threading.Thread(target=ss.zero, args=(printNumber,))
    thread2 = threading.Thread(target=ss.even, args=(printNumber,))
    thread3 = threading.Thread(target=ss.odd, args=(printNumber,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()