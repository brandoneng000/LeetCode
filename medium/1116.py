from typing import Callable
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.flag = True
        self.zero_sem = Semaphore(1)
        self.even_sem = Semaphore(1)
        self.odd_sem = Semaphore(1)
        self.even_sem.acquire()
        self.odd_sem.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.zero_sem.acquire()
            printNumber(0)
            if self.flag:
                self.odd_sem.release()
            else:
                self.even_sem.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
            self.flag = not self.flag
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
            self.flag = not self.flag