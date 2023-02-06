from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = (-1, -1)
        board_size = 8
        result = 0

        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 'R':
                    rook = (row, col)
                    break

            if rook != (-1, -1):
                break
        
        print(rook)
        col = rook[1]
        row = rook[0]
        while(col >= 0 and board[row][col] != 'B'):
            if board[row][col] == 'p':
                result += 1
                break
            col -= 1
        col = rook[1]
        while(col < board_size and board[row][col] != 'B'):
            if board[row][col] == 'p':
                result += 1
                break
            col += 1
        col = rook[1]
        while(row >= 0 and board[row][col] != 'B'):
            if board[row][col] == 'p':
                result += 1
                break
            row -= 1
        row = rook[0]
        while(row < board_size and board[row][col] != 'B'):
            if board[row][col] == 'p':
                result += 1
                break
            row += 1
        
        return result
        


def main():
    sol = Solution()
    print(sol.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
    print(sol.numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
    print(sol.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))

if __name__ == '__main__':
    main()