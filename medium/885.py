from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        RIGHT, DOWN, LEFT, UP = 0,1,2,3
        distance = 0
        adj_row, adj_col = 0, 1

        d = 0
        res = [[rStart, cStart]]

        while len(res) < rows * cols:
            if d == RIGHT:
                distance += 1
                adj_row, adj_col = 0, 1
            elif d == DOWN:
                adj_row, adj_col = 1, 0
            elif d == LEFT:
                distance += 1
                adj_row, adj_col = 0, -1
            elif d == UP:
                adj_row, adj_col = -1, 0

            d = (d + 1) % 4
            for _ in range(1, distance + 1):
                cStart += adj_col
                rStart += adj_row

                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
        
        return res


def main():
    sol = Solution()
    print(sol.spiralMatrixIII(rows = 1, cols = 4, rStart = 0, cStart = 0))
    print(sol.spiralMatrixIII(rows = 5, cols = 6, rStart = 1, cStart = 4))

if __name__ == '__main__':
    main()