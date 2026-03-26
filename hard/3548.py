from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(freq: List[int], grid: List[List[int]], r1: int, r2: int, c1: int, c2: int, diff: int):
            rows = r2 - r1 + 1
            cols = c2 - c1 + 1

            if rows * cols == 1:
                return False
            
            if rows == 1:
                return grid[r1][c1] == diff or grid[r2][c2] == diff
            
            if cols == 1:
                return grid[r1][c1] == diff or grid[r2][c2] == diff
            
            return freq[diff] > 0

        m, n = len(grid), len(grid[0])
        total = 0

        top = [0] * 100001
        bottom = [0] * 100001
        left = [0] * 100001
        right = [0] * 100001

        for row in grid:
            for num in row:
                total += num
                bottom[num] += 1
                right[num] += 1
        
        sum_top = 0

        for i in range(m - 1):
            for j in range(n):
                num = grid[i][j]
                sum_top += num

                top[num] += 1
                bottom[num] -= 1
            
            sum_bottom = total - sum_top

            if sum_top == sum_bottom:
                return True
            
            diff = abs(sum_top - sum_bottom)

            if diff <= 100000:
                if sum_top > sum_bottom:
                    if check(top, grid, 0, i, 0, n - 1, diff):
                        return True
                else:
                    if check(bottom, grid, i + 1, m - 1, 0, n - 1, diff):
                        return True
        
        sum_left = 0

        for j in range(n - 1):
            for i in range(m):
                num = grid[i][j]
                sum_left += num
                
                left[num] += 1
                right[num] -= 1
            
            sum_right = total - sum_left

            if sum_left == sum_right:
                return True
            
            diff = abs(sum_left - sum_right)

            if diff <= 100000:
                if sum_left > sum_right:
                    if check(left, grid, 0, m - 1, 0, j, diff):
                        return True
                else:
                    if check(right, grid, 0, m - 1, j + 1, n - 1, diff):
                        return True
        
        return False
        
def main():
    sol = Solution()
    print(sol.canPartitionGrid([[100000],[100000],[100000],[100000],[1]]))
    print(sol.canPartitionGrid([[1,4],[2,3]]))
    print(sol.canPartitionGrid([[1,2],[3,4]]))
    print(sol.canPartitionGrid([[1,2,4],[2,3,5]]))

if __name__ == '__main__':
    main()