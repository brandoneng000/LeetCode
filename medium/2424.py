class LUPrefix:

    def __init__(self, n: int):
        self.videos = [False] * (n + 1)
        self.cur = 0        

    def upload(self, video: int) -> None:
        self.videos[video - 1] = True

        while self.videos[self.cur]:
            self.cur += 1

    def longest(self) -> int:
        return self.cur
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()