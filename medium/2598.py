from typing import List
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder = [0] * value
        res = 0

        for num in nums:
            r = num % value
            remainder[r] += 1

        while remainder[res % value]:
            remainder[res % value] -= 1
            res += 1
        
        return res


    # def findSmallestInteger(self, nums: List[int], value: int) -> int:
    #     count = Counter([num % value for num in nums])
    #     res = 0

    #     while count[res % value]:
    #         count[res % value] -= 1
    #         res += 1
        
    #     return res

def main():
    sol = Solution()
    print(sol.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5))
    print(sol.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7))

if __name__ == '__main__':
    main()