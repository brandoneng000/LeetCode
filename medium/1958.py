from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            r = rMove + dr
            c = cMove + dc
            count = 2

            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '.' or count < 3 and board[r][c] == color:
                    break

                if board[r][c] == color:
                    return True
                
                count += 1
                r += dr
                c += dc
        
        return False

        
def main():
    sol = Solution()
    print(sol.checkMove(board = [[".",".",".","B",".",".",".","."],
                                 [".",".",".","W",".",".",".","."],
                                 [".",".",".","W",".",".",".","."],
                                 [".",".",".","W",".",".",".","."],
                                 ["W","B","B",".","W","W","W","B"],
                                 [".",".",".","B",".",".",".","."],
                                 [".",".",".","B",".",".",".","."],
                                 [".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"))
    print(sol.checkMove(board = [[".",".",".",".",".",".",".","."],
                                 [".","B",".",".","W",".",".","."],
                                 [".",".","W",".",".",".",".","."],
                                 [".",".",".","W","B",".",".","."],
                                 [".",".",".",".",".",".",".","."],
                                 [".",".",".",".","B","W",".","."],
                                 [".",".",".",".",".",".","W","."],
                                 [".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"))
    print(sol.checkMove(board = [["B","B",".",".","B","W","W","."],
                                 [".","W","W",".","B","W","B","B"],
                                 [".","W","B","B","W","A","W","."],
                                 ["B",".",".","B","W","W","W","."],
                                 ["W","W","W","B","W",".","B","W"],
                                 [".",".",".","W",".","W",".","B"],
                                 ["B","B","W","B","B","W","W","B"],
                                 ["W",".","W","W",".","B",".","W"]], rMove = 2, cMove = 5, color = "W"))

if __name__ == '__main__':
    main()