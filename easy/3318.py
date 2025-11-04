from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        for start in range(n - k + 1):
            # print(nums[start: start + k])
            count = Counter(nums[start: start + k])
            res.append(sum((x * c) for x, c in sorted(count.items(), key=lambda x: (-x[1], -x[0]))[:x]))
        
        return res
        
def main():
    sol = Solution()
    print(sol.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
    print(sol.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2))

if __name__ == '__main__':
    main()