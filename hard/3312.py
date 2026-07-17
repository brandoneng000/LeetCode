from typing import List
from math import gcd
from collections import Counter
from bisect import bisect_right, bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        cnt = [0] * (m + 1)
        res = []

        for num in nums:
            cnt[num] += 1
        
        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                cnt[i] += cnt[j]
        
        for i in range(1, m + 1):
            cnt[i] = cnt[i] * (cnt[i] - 1) // 2

        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                cnt[i] -= cnt[j]
        
        for i in range(1, m + 1):
            cnt[i] += cnt[i - 1]
        
        for q in queries:
            q += 1
            index = bisect_left(cnt, q)
            res.append(index)

        return res


    # def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
    #     n = len(nums)
    #     gcd_count = Counter()
    #     gcd_vals = [0]
    #     gcd_div = [0]
    #     res = []

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             gcd_count[gcd(nums[i], nums[j])] += 1
        
    #     for d, c in sorted(gcd_count.items()):
    #         gcd_vals.append(gcd_vals[-1] + c)
    #         gcd_div.append(d)
        
    #     for q in queries:
    #         index = bisect_right(gcd_vals, q)
    #         res.append(gcd_div[index])
        
    #     return res


    # def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
    #     n = len(nums)
    #     gcd_list = []
    #     res = []

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             gcd_list.append(gcd(nums[i], nums[j]))
        
    #     gcd_list.sort()

    #     for q in queries:
    #         res.append(gcd_list[q])
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.gcdValues(nums = [2,3,4], queries = [0,2,2]))
    print(sol.gcdValues(nums = [4,4,2,1], queries = [5,3,1,0]))
    print(sol.gcdValues(nums = [2,2], queries = [0,0]))

if __name__ == '__main__':
    main()