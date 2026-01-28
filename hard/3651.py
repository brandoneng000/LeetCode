from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda x: grid[x[0]][x[1]])
        costs = [[float("inf")] * n for _ in range(m)]

        for t in range(k + 1):
            min_cost = float("inf")
            j = 0

            for i in range(len(points)):
                min_cost = min(min_cost, costs[points[i][0]][points[i][1]])
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]] == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = min_cost
                j = i + 1
            
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(costs[i][j], costs[i + 1][j] + grid[i + 1][j])
                    if j != n - 1:
                        costs[i][j] = min(costs[i][j], costs[i][j + 1] + grid[i][j + 1])
        
        return costs[0][0]
        
def main():
    sol = Solution()
    print(sol.minCost(grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2))
    print(sol.minCost(grid = [[1,2],[2,3],[3,4]], k = 1))

if __name__ == '__main__':
    main()