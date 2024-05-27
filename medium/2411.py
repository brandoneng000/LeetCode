from typing import List
from collections import Counter

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        last = [0] * 32

        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            
            res[i] = max(1, max(last) - i + 1)

        return res

def main():
    sol = Solution()
    print(sol.smallestSubarrays([8,10,8]))
    print(sol.smallestSubarrays([1,0,2,1,3]))
    print(sol.smallestSubarrays([1,2]))

if __name__ == '__main__':
    main()