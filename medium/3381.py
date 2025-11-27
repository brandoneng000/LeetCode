from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        res = -float('inf')
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            mod = (i + 1) % k

            if min_prefix[mod] != float('inf'):
                res = max(res, prefix - min_prefix[mod])
            
            min_prefix[mod] = min(min_prefix[mod], prefix)
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxSubarraySum(nums = [1,2], k = 1))
    print(sol.maxSubarraySum(nums = [-1,-2,-3,-4,-5], k = 4))
    print(sol.maxSubarraySum(nums = [-5,1,2,-3,4], k = 2))

if __name__ == '__main__':
    main()