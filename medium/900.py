from typing import List
import collections

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encode = collections.deque(encoding)

    def next(self, n: int) -> int:     
        while self.encode:
            if self.encode[0] < n:
                n -= self.encode.popleft()
                self.encode.popleft()
            elif self.encode[0] == n:
                self.encode.popleft()
                return self.encode.popleft()
            else:
                self.encode[0] -= n
                return self.encode[1]

        return -1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)