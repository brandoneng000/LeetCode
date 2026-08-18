from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter()
        res = -1

        for i in range(n - k + 1):
            for j in set(nums[i: i + k]):
                freq[j] += 1

        for num in freq:
            if freq[num] == 1:
                res = max(res, num)

        return res

def main():
    sol = Solution()
    print(sol.largestInteger(nums = [3,9,2,1,7], k = 3))
    print(sol.largestInteger(nums = [3,9,7,2,1,7], k = 4))
    print(sol.largestInteger(nums = [0,0], k = 1))
    print(sol.largestInteger(nums = [0,0], k = 2))

if __name__ == '__main__':
    main()