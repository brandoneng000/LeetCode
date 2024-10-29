from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int, grid: List[List[int]], dp: dict):
            
            if (row, col) in dp:
                return dp[(row, col)]

            res = 0

            for dir in directions:
                r = row + dir
                c = col + 1

                if 0 <= r < m and 0 <= c < n and grid[row][col] < grid[r][c]:
                    res = max(res, 1 + dfs(r, c, grid, dp))

            dp[(row, col)] = res
            return res

        m, n = len(grid), len(grid[0])
        directions = [-1, 0, 1]
        dp = {}
        res = 0

        for i in range(m):
            cur_moves = dfs(i, 0, grid, dp)
            res = max(res, cur_moves)
        
        return res

    # def maxMoves(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     res = 0
    #     cur = set([(i, 0) for i in range(m)])

    #     while cur:
    #         next = set()

    #         for row, col in cur:
    #             c = col + 1

    #             for dr in [-1, 0, 1]:
    #                 r = row + dr
                    
    #                 if 0 <= r < m and c < n and grid[row][col] < grid[r][c]:
    #                     next.add((r, c))

    #         if next:
    #             res += 1
            
    #         cur = next
            
    #     return res


        
def main():
    sol = Solution()
    print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
    print(sol.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))

if __name__ == '__main__':
    main()