from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prefix = [[0 for j in range(n + 1)] for i in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                prefix[i][j + 1] = prefix[i][j] + grid[i][j]
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                top = prefix[i - 1][j + 2] - prefix[i - 1][j - 1]
                middle = grid[i][j]
                bottom = prefix[i + 1][j + 2] - prefix[i + 1][j - 1]
                res = max(res, top + middle + bottom)
        
        return res
        

def main():
    sol = Solution()
    print(sol.maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))
    print(sol.maxSum([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()