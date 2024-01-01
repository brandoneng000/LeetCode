class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_live = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return

        if self.tokens[tokenId] + self.time_live > currentTime:
            self.tokens[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0

        for token in self.tokens:
            if self.tokens[token] + self.time_live > currentTime:
                res += 1

        return res
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)