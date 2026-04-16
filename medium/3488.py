from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        INF = 10 ** 33
        indices = defaultdict(list)
        res = []

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        for q in queries:
            num = nums[q]
            v = indices[num]

            if len(indices[num]) == 1:
                res.append(-1)
                continue
            
            index = bisect_left(v, q)
            result = INF
            
            left = v[(index - 1) % len(v)]
            d1 = abs(q - left)
            result = min(result, min(d1, n - d1))

            right = v[(index + 1) % len(v)]
            d2 = abs(q - right)
            result = min(result, min(d2, n - d2))

            res.append(result)
        
        return res


        
def main():
    sol = Solution()
    print(sol.solveQueries(nums = [1,3,1,4,1,3,2], queries = [0,3,5]))
    print(sol.solveQueries(nums = [1,2,3,4], queries = [0,1,2,3]))

if __name__ == '__main__':
    main()