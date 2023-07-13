from typing import List
from string import ascii_lowercase, ascii_uppercase

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        p = len(pattern)

        for word in queries:
            index = 0
            for letter in word:
                if letter in ascii_uppercase and (index == p or letter != pattern[index]):
                    index = -1
                    break
                if index < p and letter == pattern[index]:
                    index += 1
            res.append(index == p)

        return res

def main():
    sol = Solution()
    print(sol.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
    print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
    print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))

if __name__ == '__main__':
    main()