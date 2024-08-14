from typing import List
from collections import defaultdict

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        indexes = defaultdict(list)
        res = n

        for i in range(n):
            indexes[nums[i]].append(i)
        
        for num in indexes:
            if len(indexes[num]) == 1:
                continue

            max_dist = indexes[num][0] + n - indexes[num][-1]

            for i in range(len(indexes[num]) - 1):
                max_dist = max(max_dist, indexes[num][i + 1] - indexes[num][i])
            
            res = min(res, max_dist)
        
        return res // 2
        
def main():
    sol = Solution()
    print(sol.minimumSeconds([1,2,1,2]))
    print(sol.minimumSeconds([2,1,3,3,2]))
    print(sol.minimumSeconds([5,5,5,5]))

if __name__ == '__main__':
    main()