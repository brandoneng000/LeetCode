from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0 if nums[0] == 0 else 1

        for i in range(n - 1):

            if i + 1 < nums[i + 1] and i + 1 > nums[i]:
                res += 1
        
        return res + (n > nums[-1])
        
def main():
    sol = Solution()
    print(sol.countWays([1,1]))
    print(sol.countWays([6,0,3,3,6,7,2,7]))

if __name__ == '__main__':
    main()