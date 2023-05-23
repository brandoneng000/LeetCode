class MyCircularQueue:
    def __init__(self, k: int):
        self.circular_q = [-1] * k
        self.cur_index = 0
        self.end_index = 0
        self.max_size = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self.circular_q[self.end_index] = value
        self.end_index = (self.end_index + 1) % self.max_size
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.circular_q[self.cur_index] = -1
        self.cur_index = (self.cur_index + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.circular_q:
            return self.circular_q[self.cur_index]
        return -1

    def Rear(self) -> int:
        if self.circular_q:
            return self.circular_q[self.end_index - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()