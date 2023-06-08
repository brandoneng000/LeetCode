from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_marks, o_marks = 0, 0
        x_wins, o_wins = False, False
        for row in board:
            if row == 'XXX':
                x_wins = True
            if row == 'OOO':
                o_wins = True

            for c in row:
                if c == 'X':
                    x_marks += 1
                elif c == 'O':
                    o_marks += 1

        for i in range(3):
            cur_mark = board[0][i]
            count = 1
            for j in range(1, 3):
                if cur_mark == board[j][i]:
                    count += 1
            if count == 3:
                if cur_mark == 'X':
                    x_wins = True
                elif cur_mark == 'O':
                    o_wins = True
        
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1]== board[2][0]:
            if board[1][1] == 'X':
                x_wins = True
            elif board[1][1] == 'O':
                o_wins = True
            
        if x_wins and o_wins:
            return False
        elif x_wins and x_marks == o_marks:
            return False
        elif o_wins and x_marks != o_marks:
            return False

        if o_marks > x_marks:
            return False
        elif o_marks + 2 <= x_marks:
            return False
        
        return True

def main():
    sol = Solution()
    print(sol.validTicTacToe(["X  ","   ","  O"]))
    print(sol.validTicTacToe(["XOX","OOX","XO "]))
    print(sol.validTicTacToe(["XOX","OXO","XOX"]))
    print(sol.validTicTacToe(["O  ","   ","   "]))
    print(sol.validTicTacToe(["XOX"," X ","   "]))
    print(sol.validTicTacToe(["XOX","O O","XOX"]))

if __name__ == '__main__':
    main()