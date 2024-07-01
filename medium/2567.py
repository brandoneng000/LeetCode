from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
        

def main():
    sol = Solution()
    print(sol.minimizeSum([1,4,7,8,5]))
    print(sol.minimizeSum([1,4,3]))

if __name__ == '__main__':
    main()