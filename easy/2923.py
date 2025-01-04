from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        teams = [0] * m

        for i in range(n):
            for j in range(m):
                teams[j] += grid[i][j]
        
        return teams.index(0)
        
def main():
    sol = Solution()
    print(sol.findChampion([[0,1],[0,0]]))
    print(sol.findChampion([[0,0,1],[1,0,1],[0,0,0]]))

if __name__ == '__main__':
    main()