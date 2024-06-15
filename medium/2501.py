from typing import List
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()
        res = -1

        for num in nums_set:
            if num in visited:
                continue
            cur = 1

            temp = num
            while sqrt(temp) in nums_set:
                temp = sqrt(temp)
                visited.add(temp)
                cur += 1
            
            temp = num
            while temp * temp in nums_set:
                temp *= temp
                visited.add(temp)
                cur += 1
            
            if cur > 1:
                res = max(res, cur)
        
        return res

        
def main():
    sol = Solution()
    print(sol.longestSquareStreak(nums = [2, 4]))
    print(sol.longestSquareStreak(nums = [4,3,6,16,8,2]))
    print(sol.longestSquareStreak(nums = [2,3,5,6,7]))

if __name__ == '__main__':
    main()