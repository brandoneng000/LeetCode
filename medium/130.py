from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def search(r: int, c: int):
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'X':
                return
            elif 0 <= r < m and 0 <= c < n and (r, c) not in safe:
                safe.add((r, c))
                for dir_x, dir_y in directions:
                    search(r + dir_x, c + dir_y)
        
        for i in range(n):
            search(0, i)
            search(m - 1, i)

        for j in range(m):
            search(j, 0)
            search(j, n - 1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in safe:
                    board[i][j] = 'X'
        
        
        



def main():
    sol = Solution()
    val = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(val)
    print(val)
    val = [["X","X","X","X"],["X","O","O","O"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(val)
    print(val)
    val = [["X"]]
    sol.solve(val)
    print(val)

if __name__ == '__main__':
    main()