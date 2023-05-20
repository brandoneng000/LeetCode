from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        cols, rows = len(board[0]), len(board)
        stack = [click]

        def bfs(r: int, c: int):
            mines = 0
            temp = []
            for x, y in directions:
                if 0 <= c + x < cols and 0 <= r + y < rows:
                    val = board[r + y][c + x]
                    if val == 'M':
                        mines += 1
                    elif val == 'E':
                        temp.append((r + y, c + x))
            if mines != 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                stack.extend(temp)
        
        while stack:
            r, c = stack.pop()
            if board[r][c] != 'M':
                bfs(r, c)
            else:
                board[r][c] = 'X'
                break
        
        return board
        

def main():
    sol = Solution()
    print(sol.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))
    print(sol.updateBoard(board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]))

if __name__ == '__main__':
    main()