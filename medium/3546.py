from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def pivot(nums: List[int]):
            left = 0
            right = sum(nums)

            for num in nums:
                left += num
                right -= num

                if left == right:
                    return True

            return False

        horizontal = []
        vertical = []

        for row in grid:
            horizontal.append(sum(row))
        
        for col in zip(*grid):
            vertical.append(sum(col))
        
        return pivot(horizontal) or pivot(vertical)
        
        
def main():
    sol = Solution()
    print(sol.canPartitionGrid(grid = [[1,4],[2,3]]))
    print(sol.canPartitionGrid(grid = [[1,3],[2,4]]))

if __name__ == '__main__':
    main()