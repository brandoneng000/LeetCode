from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for num in nums:
            count += num == 1
        
        if count:
            return n - count
        
        for steps in range(n):
            for i in range(n - steps - 1):
                nums[i] = gcd(nums[i], nums[i + 1])
                if nums[i] == 1:
                    return steps + n
        
        return -1

def main():
    sol = Solution()
    print(sol.minOperations([2,6,3,4]))
    print(sol.minOperations([2,10,6,14]))

if __name__ == '__main__':
    main()