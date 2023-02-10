from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        current_player_moves = []
        final_move = moves[-1]
        current_player = (len(moves) + 1) % 2

        for index in range(len(moves)):
            if index % 2 == current_player:
                current_player_moves.append(moves[index])

        if [0,0] in current_player_moves and [1,1] in current_player_moves and [2, 2] in current_player_moves:
            return 'A' if current_player == 0 else 'B'
        elif [0,2] in current_player_moves and [1,1] in current_player_moves and [2, 0] in current_player_moves:
            return 'A' if current_player == 0 else 'B'
        elif [final_move[0] , 0] in current_player_moves and [final_move[0] , 1] in current_player_moves and [final_move[0] , 2] in current_player_moves :
            return 'A' if current_player == 0 else 'B'
        elif [0 , final_move[1]] in current_player_moves and [1 , final_move[1]] in current_player_moves and [2 , final_move[1]] in current_player_moves :
            return 'A' if current_player == 0 else 'B'

        if len(moves) == 9:
            return "Draw"
        return "Pending"

def main():
    sol = Solution()
    print(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(sol.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
    print(sol.tictactoe([[0,1],[2,0],[2,2],[2,1]]))
    print(sol.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))

if __name__ == '__main__':
    main()