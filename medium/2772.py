from typing import List
from collections import deque

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        cur = 0

        for i, num in enumerate(nums):
            if cur > num:
                return False
            
            nums[i], cur = num - cur, num

            if i >= k - 1:
                cur -= nums[i - k + 1]
        
        return cur == 0

def main():
    sol = Solution()
    print(sol.checkArray(nums = [2,2,3,1,1,0], k = 3))
    print(sol.checkArray(nums = [1,3,1,1], k = 2))

if __name__ == '__main__':
    main()