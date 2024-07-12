from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_indexes = defaultdict(list)
        res = [0] * n

        for i, num in enumerate(nums):
            nums_indexes[num].append(i)
        
        for num in nums_indexes:
            m = len(nums_indexes[num])
            left = 0
            right = sum(nums_indexes[num])
            for i in range(m):
                res[nums_indexes[num][i]] = (nums_indexes[num][i] * i - left) + (right - nums_indexes[num][i] * (m - i))
                left += nums_indexes[num][i]
                right -= nums_indexes[num][i]
        
        return res
        
def main():
    sol = Solution()
    print(sol.distance([1,3,1,1,2]))
    print(sol.distance([0,5,3]))

if __name__ == '__main__':
    main()