from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        def helper(prev: int, mask: int):
            if mask == (1 << n) - 1:
                return 1
            
            if (prev, mask) in dp:
                return dp[(prev, mask)]
            
            count = 0

            for i in range(n):
                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    count = (count + helper(nums[i], mask | (1 << i))) % mod

            dp[(prev, mask)] = count
            return count

        n = len(nums)
        mod = 1000000007
        dp = {}

        return helper(1, 0) % mod
        
def main():
    sol = Solution()
    print(sol.specialPerm([2,3,6]))
    print(sol.specialPerm([1,4,3]))

if __name__ == '__main__':
    main()