class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if self.size == len(self.stack):
            return
        
        self.stack.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop() + self.inc.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.inc))):
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)