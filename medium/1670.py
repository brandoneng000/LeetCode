class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.arr.insert(len(self.arr) // 2, val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        if self.arr:
            return self.arr.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.arr:
            return self.arr.pop((len(self.arr) - 1) // 2)
        return -1

    def popBack(self) -> int:
        if self.arr:
            return self.arr.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()