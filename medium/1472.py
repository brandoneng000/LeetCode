import collections

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = collections.deque()
        self.home = homepage
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = collections.deque()

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.history) > 1:
                self.future.appendleft(self.history.pop())
            else:
                break
        
        return self.history[-1]
        
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.future:
                self.history.append(self.future.popleft())
            else:
                break

        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)