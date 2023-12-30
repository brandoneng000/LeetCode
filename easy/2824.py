from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                res += (nums[i] + nums[j]) < target
        
        return res
        
def main():
    sol = Solution()
    print(sol.countPairs(nums = [-1,1,2,3,1], target = 2))
    print(sol.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))

if __name__ == '__main__':
    main()