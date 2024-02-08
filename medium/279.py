from typing import List
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        squares = []
        i = 1

        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        res = 0
        q = deque([n])
        
        while q:
            res += 1
            size = len(q)

            for _ in range(size):
                cur = q.popleft()
                for s in squares:
                    if s == cur:
                        return res
                    if cur < s:
                        break
                    q.append(cur - s)
        
        return res

    # def numSquares(self, n: int) -> int:
    #     cache = [n] * (n + 1)
    #     cache[0] = 0

    #     for i in range(1, n + 1):
    #         j = 1
    #         while(j * j <= n):
    #             cache[i] = min(cache[i], cache[i - j * j] + 1)
    #             j += 1
        
    #     return cache[n]

    # def numSquares(self, n: int) -> int:
    #     def helper(n):
    #         if not n:
    #             return 0
    #         if n < 0:
    #             return 100000
    #         if cache[n] != -1:
    #             return cache[n]

    #         res = n
    #         i = 1
    #         while i * i <= n:
    #             res = min(res, helper(n - (i * i)))
    #             i += 1

    #         cache[n] = res + 1
    #         return cache[n]
        
    #     cache = [-1] * (n + 1)
    #     return helper(n)


def main():
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(1))
    print(sol.numSquares(38))

if __name__ == '__main__':
    main()