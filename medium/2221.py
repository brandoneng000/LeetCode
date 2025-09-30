from typing import List
from math import comb

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            res = (res + comb(n - 1, i) * nums[i]) % 10
        
        return res

    # def triangularSum(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     while n > 1:
    #         next = []

    #         for i in range(n - 1):
    #             next.append((nums[i] + nums[i + 1]) % 10)
            
    #         nums = next
    #         n -= 1
        
    #     return nums[0]


    # def triangularSum(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cur = nums.copy()

    #     for i in range(n - 1, 0, -1):
    #         next = [0] * i

    #         for j in range(len(cur) - 1):
    #             next[j] = cur[j] + cur[j + 1] 
            
    #         cur = next
        
    #     return cur[0] % 10

def main():
    sol = Solution()
    print(sol.triangularSum([1,2,3,4,5]))
    print(sol.triangularSum([5]))

if __name__ == '__main__':
    main()