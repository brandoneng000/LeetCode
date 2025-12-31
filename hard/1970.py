from typing import List

class DSU:
    def __init__(self, n: int):
        self.root = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self. root[x]

    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return
        if self.size[rx] > self.size[ry]:
            rx, ry = ry, rx

        self.root[rx] = ry
        self.size[ry] += self.size[rx]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        grid = [[0] * col for _ in range(row)]

        for i in range(row * col):
            r = cells[i][0] - 1
            c = cells[i][1] - 1
            grid[r][c] = 1

            id1 = r * col + c + 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    id2 = nr * col + nc + 1
                    dsu.union(id1, id2)
            
            if c == 0:
                dsu.union(0, id1)
            
            if c == col - 1:
                dsu.union(row * col + 1, id1)
            
            if dsu.find(0) == dsu.find(row * col + 1):
                return i
        
        return -1

        
def main():
    sol = Solution()
    print(sol.latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]))
    print(sol.latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]))
    print(sol.latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))

if __name__ == '__main__':
    main()