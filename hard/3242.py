from typing import List

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.adj = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.diag = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    def add_sides(self, row: int, col: int, direction: List[List[int]]):
        res = 0

        for dr, dc in direction:
            r = row + dr
            c = col + dc

            if 0 <= r < self.n and 0 <= c < self.m:
                res += self.grid[r][c]
        
        return res

    def adjacentSum(self, value: int) -> int:
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == value:
                    return self.add_sides(i, j, self.adj)

    def diagonalSum(self, value: int) -> int:
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == value:
                    return self.add_sides(i, j, self.diag)


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)