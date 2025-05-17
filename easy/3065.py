from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        index = bisect_left(nums, k)

        return index
        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [2,11,10,1,3], k = 10))
    print(sol.minOperations(nums = [1,1,2,4,9], k = 1))
    print(sol.minOperations(nums = [1,1,2,4,9], k = 9))

if __name__ == '__main__':
    main()