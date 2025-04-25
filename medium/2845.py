from typing import List
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = Counter([0])
        res = 0
        prefix = 0

        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += count[(prefix - k + modulo) % modulo]
            count[prefix % modulo] += 1
        
        return res


    # def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
    #     n = len(nums)
    #     prefix = [0] + [nums[i] % modulo == k for i in range(n)]
    #     count = Counter()
    #     res = 0

    #     for i in range(1, n + 1):
    #         prefix[i] = (prefix[i] + prefix[i - 1]) % modulo
        
    #     for i in range(n + 1):
    #         j = prefix[i] - k
    #         res += count[j % modulo]
    #         count[prefix[i] % modulo] += 1
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1))
    print(sol.countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0))

if __name__ == '__main__':
    main()