from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = set()

        for i in range(m):
            cur = set()
            for j in range(n):
                if grid[i][j]:
                    cur.add(i * n + j)
            
            if len(cur) > 1:
                res.update(cur)
        
        for j in range(n):
            cur = set()
            for i in range(m):
                if grid[i][j]:
                    cur.add(i * n + j)
            
            if len(cur) > 1:
                res.update(cur)

        return len(res)

    # def countServers(self, grid: List[List[int]]) -> int:
    #     rows, cols = list(map(sum, grid)), list(map(sum, zip(*grid)))
    #     res = 0

    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j]:
    #                 res += (rows[i] + cols[j]) > 2
        
    #     return res

def main():
    sol = Solution()
    print(sol.countServers([[1,0],[0,1]]))
    print(sol.countServers([[1,0],[1,1]]))
    print(sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))

if __name__ == '__main__':
    main()