from typing import List
from math import lcm

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            cur = nums[i]
            for j in range(i, n):
                cur = lcm(cur, nums[j])

                if cur == k:
                    res += 1
                elif cur > k:
                    break
                
        return res
        
        
def main():
    sol = Solution()
    print(sol.subarrayLCM(nums = [3,6,2,7,1], k = 6))
    print(sol.subarrayLCM(nums = [3], k = 2))

if __name__ == '__main__':
    main()