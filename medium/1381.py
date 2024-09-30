# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.size = maxSize
#         self.stack = []
#         self.inc = { i: 0 for i in range(maxSize) }

#     def push(self, x: int) -> None:
#         if self.size == len(self.stack):
#             return
        
#         self.stack.append(x)

#     def pop(self) -> int:
#         if self.stack:
#             temp = self.inc[len(self.stack) - 1]
#             self.inc[len(self.stack) - 1] = 0
#             return self.stack.pop() + temp
#         return -1

#     def increment(self, k: int, val: int) -> None:
#         for i in range(min(k, len(self.stack))):
#             self.inc[i] += val

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