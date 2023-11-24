from typing import List
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque([0])

        for i in range(1, n):
            nums[i] = nums[q[0]] + nums[i]

            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)

            if i - q[0] >= k: 
                q.popleft()
            
        return nums[n - 1]

    
def main():
    sol = Solution()
    print(sol.maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
    print(sol.maxResult(nums = [10,-5,-2,4,0,3], k = 3))
    print(sol.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))

if __name__ == '__main__':
    main()