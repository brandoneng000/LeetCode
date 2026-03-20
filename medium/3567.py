from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        INF = 10 ** 33
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                kgrid = []

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        kgrid.append(grid[x][y])
                
                kmin = INF
                kgrid.sort()

                for t in range(1, len(kgrid)):
                    if kgrid[t] == kgrid[t - 1]:
                        continue
                    kmin = min(kmin, kgrid[t] - kgrid[t - 1])
                
                if kmin != INF:
                    res[i][j] = kmin
        
        return res
        
def main():
    sol = Solution()
    print(sol.minAbsDiff(grid = [[1,8],[3,-2]], k = 2))
    print(sol.minAbsDiff(grid = [[3,-1]], k = 1))
    print(sol.minAbsDiff(grid = [[1,-2,3],[2,3,5]], k = 2))

if __name__ == '__main__':
    main()