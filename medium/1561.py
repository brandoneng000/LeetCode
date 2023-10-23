from typing import List
import collections

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        alice = n - 1
        res = 0

        while n:
            res += piles[alice - 1]
            alice -= 2
            n -= 3
        
        return res
        

    # def maxCoins(self, piles: List[int]) -> int:
    #     piles.sort()
    #     deque = collections.deque(piles)
    #     res = 0

    #     while deque:
    #         deque.pop()
    #         res += deque.pop()
    #         deque.popleft()
        
    #     return res
        

def main():
    sol = Solution()
    print(sol.maxCoins([2,4,1,2,7,8]))
    print(sol.maxCoins([2,4,5]))
    print(sol.maxCoins([9,8,7,6,5,1,2,3,4]))

if __name__ == '__main__':
    main()