from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        
        for i in range(n // 2):
            res += max(0, nums[i] - k)
        
        for i in range(n // 2, n):
            res += max(0, k - nums[i])
        
        return res
                

        
def main():
    sol = Solution()
    print(sol.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 4))
    print(sol.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 7))
    print(sol.minOperationsToMakeMedianK(nums = [1,2,3,4,5,6], k = 4))

if __name__ == '__main__':
    main()