from typing import List
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        q = collections.deque([(0, 0)])
        visited = { (0, 0) }
        distance = 1

        while q:
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                if row == n - 1 and col == n - 1:
                    return distance
                
                for adj_r, adj_c in directions:
                    r = row + adj_r
                    c = col + adj_c
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
            
            distance += 1
        
        return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     if grid[0][0] == 1:
    #         return -1
        
    #     n = len(grid)
    #     directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    #     distance = [[float('inf')] * n for _ in range(n)]        

    #     def dfs(row: int, col: int, dist: int):
    #         distance[row][col] = dist
    #         for adj_r, adj_c in directions:
    #             r = row + adj_r
    #             c = col + adj_c
    #             if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and distance[r][c] > dist + 1:
    #                 dfs(r, c, dist + 1)
        
    #     dfs(0, 0, 1)
    #     return distance[n - 1][n - 1] if distance[n - 1][n - 1] != float('inf') else -1


def main():
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,1,1],[1,1,1],[1,1,0]]))

if __name__ == '__main__':
    main()