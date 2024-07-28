from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 1000000007
        n = len(nums)

        for i in range(n):
            nums[i] += (1 if s[i] == 'R' else -1) * d
        
        nums.sort()
        res = 0
        prefix = 0

        for i in range(n):
            res += (i * nums[i] - prefix) % mod
            prefix += nums[i]
        
        return res % mod
        
def main():
    sol = Solution()
    print(sol.sumDistance(nums = [-2,0,2], s = "RLL", d = 3))
    print(sol.sumDistance(nums = [1,0], s = "RL", d = 2))

if __name__ == '__main__':
    main()