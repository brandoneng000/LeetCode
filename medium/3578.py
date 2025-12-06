from typing import List
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        n = len(nums)
        prefix = [0] * (n + 2)
        prefix[1] = 1

        q_max = deque()
        q_min = deque()

        l = 0
        res = 0

        for r, x in enumerate(nums):

            while q_max and q_max[-1] < x:
                q_max.pop()
            q_max.append(x)
        
            while q_min and q_min[-1] > x:
                q_min.pop()
            q_min.append(x)

            while q_max[0] - q_min[0] > k:
                y = nums[l]

                if q_max[0] == y:
                    q_max.popleft()
                if q_min[0] == y:
                    q_min.popleft()
                l += 1
            
            res = (prefix[r + 1] - prefix[l]) % mod
            prefix[r + 2] = (prefix[r + 1] + res) % mod
        
        return res
                


        
def main():
    sol = Solution()
    print(sol.countPartitions(nums = [9,4,1,3,7], k = 4))
    print(sol.countPartitions(nums = [3,3,4], k = 0))

if __name__ == '__main__':
    main()