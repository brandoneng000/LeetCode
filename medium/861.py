from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = (1 << n - 1) * m

        for j in range(1, n):
            cur = sum(grid[i][j] == grid[i][0] for i in range(m))
            res += max(cur, m - cur) * (1 << n - 1 - j)
        
        return res


def main():
    sol = Solution()
    print(sol.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
    print(sol.matrixScore([[0]]))

if __name__ == '__main__':
    main()