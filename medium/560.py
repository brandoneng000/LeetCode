from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = total = 0
        cache = { 0:1 }
        for i in range(len(nums)):
            total += nums[i]
            if total - k in cache:
                res += cache[total - k]
            cache[total] = cache.get(total, 0) + 1
        
        return res

def main():
    sol = Solution()
    print(sol.subarraySum(nums = [1,1,1], k = 2))
    print(sol.subarraySum(nums = [1,2,3], k = 3))

if __name__ == '__main__':
    main()