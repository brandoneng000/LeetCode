from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [-1] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        self.checkPointer()
        return self.stream[idKey - 1: self.ptr]

    def checkPointer(self):
        while self.ptr < len(self.stream):
            if self.stream[self.ptr] != -1:
                self.ptr += 1
            else:
                break

