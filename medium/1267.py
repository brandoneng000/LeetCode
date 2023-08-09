from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = list(map(sum, grid)), list(map(sum, zip(*grid)))
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += (rows[i] + cols[j]) > 2
        
        return res

def main():
    sol = Solution()
    print(sol.countServers([[1,0],[0,1]]))
    print(sol.countServers([[1,0],[1,1]]))
    print(sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))

if __name__ == '__main__':
    main()