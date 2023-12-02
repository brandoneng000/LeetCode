from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [0] * n

        for row in grid:
            for i in range(n):
                res[i] = max(res[i], len(str(row[i])))
        
        return res
        
def main():
    sol = Solution()
    print(sol.findColumnWidth(grid = [[1],[22],[333]]))
    print(sol.findColumnWidth(grid = [[-15,1,3],[15,7,12],[5,6,-2]]))

if __name__ == '__main__':
    main()