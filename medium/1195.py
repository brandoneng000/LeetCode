from typing import Callable
from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.three = Semaphore()
        self.five = Semaphore()
        self.fifteen = Semaphore()
        self.print_num = Semaphore()
        self.three.acquire()
        self.five.acquire()
        self.fifteen.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.three.acquire()
            if self.done:
                break
            printFizz()
            self.print_num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.five.acquire()
            if self.done:
                break
            printBuzz()
            self.print_num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fifteen.acquire()
            if self.done:
                break
            printFizzBuzz()
            self.print_num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            check_three = i % 3 == 0
            check_five = i % 5 == 0
            self.print_num.acquire()
            if check_three and check_five:
                self.fifteen.release()
            elif check_three:
                self.three.release()
            elif check_five:
                self.five.release()
            else:
                printNumber(i)
                self.print_num.release()
        
        self.print_num.acquire()
        self.done = True
        self.three.release()
        self.five.release()
        self.fifteen.release()