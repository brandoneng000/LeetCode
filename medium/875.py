from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            middle = (left + right) // 2
            time = sum(math.ceil(b / middle) for b in piles)
            if time <= h:
                right = middle
            else:
                left = middle + 1
        
        return left

def main():
    sol = Solution()
    print(sol.minEatingSpeed(piles = [312884470], h = 312884469))
    print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))

if __name__ == '__main__':
    main()