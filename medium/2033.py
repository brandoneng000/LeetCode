from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(num for row in grid for num in row)
        n = len(nums)
        median = nums[n // 2]
        res = 0

        for num in nums:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            res += diff // x
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.minOperations(grid = [[2,4],[6,8]], x = 2))
    print(sol.minOperations(grid = [[1,5],[2,3]], x = 1))
    print(sol.minOperations(grid = [[1,2],[3,4]], x = 2))

if __name__ == '__main__':
    main()