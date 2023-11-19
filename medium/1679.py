from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()
        res = 0

        for num in nums:
            diff = k - num
            if num in count and count[num] > 0:
                res += 1
                count[num] -= 1
            else:
                count[diff] += 1
        
        return res


def main():
    sol = Solution()
    print(sol.maxOperations(nums = [1,2,3,4], k = 5))
    print(sol.maxOperations(nums = [3,1,3,4,3], k = 6))

if __name__ == '__main__':
    main()