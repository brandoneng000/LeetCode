from typing import List
from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter()
        res = 0

        for i in range(n):
            res += count[nums[i] - i]
            count[nums[i] - i] += 1
        
        return (n * (n - 1) // 2) - res
        
        
def main():
    sol = Solution()
    print(sol.countBadPairs([4,1,3,3]))
    print(sol.countBadPairs([1,2,3,4,5]))

if __name__ == '__main__':
    main()