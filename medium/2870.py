from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(num_count: int):
            if num_count == 1:
                return -1
            elif num_count <= 3:
                return 1
            elif num_count <= 5:
                return 2
            
            return 1 + helper(num_count - 3)
        
        count = Counter(nums)
        res = 0

        for num in count:
            c = helper(count[num])

            if c == -1:
                return -1

            res += c

        return res

def main():
    sol = Solution()
    print(sol.minOperations(nums = [2,3,3,2,2,4,2,3,4]))
    print(sol.minOperations(nums = [2,1,2,2,3,3]))

if __name__ == '__main__':
    main()