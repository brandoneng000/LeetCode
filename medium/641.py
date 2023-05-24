class MyCircularDeque:

    def __init__(self, k: int):
        self.d = [-1] * k
        self.size = 0
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        if self.size > 1:
            self.head -= 1
            if self.head == -1:
                self.head = len(self.d) - 1
        self.d[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        if self.size > 1:
            self.tail = (self.tail + 1) % len(self.d)
        self.d[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        if self.head == self.tail:
            pass
        else:
            self.head = (self.head + 1) % len(self.d)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        if self.head == self.tail:
            pass
        else:
            self.tail = (self.tail - 1) % len(self.d)
        return True

    def getFront(self) -> int:
        if self.size > 0:
            return self.d[self.head]
        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.d[self.tail]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.d)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()