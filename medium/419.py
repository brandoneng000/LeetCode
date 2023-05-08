from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                res += 1
        return res
        
        # visited = set()
        # res = 0
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # def dfs(x: int, y: int, visited: set):
        #     if board[x][y] == '.':
        #         return
            
        #     for dir_x, dir_y in directions:
        #         temp_x = x + dir_x
        #         temp_y = y + dir_y
                
        #         if 0 <= temp_x < len(board) and 0 <= temp_y < len(board[0]) and \
        #             (temp_x, temp_y) not in visited and board[temp_x][temp_y] == 'X':
        #             visited.add((temp_x, temp_y))
        #             dfs(temp_x, temp_y, visited)
        
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if (i, j) not in visited and board[i][j] == 'X':
        #             res += 1
        #             dfs(i, j, visited)
        
        # return res

def main():
    sol = Solution()
    print(sol.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
    print(sol.countBattleships([["."]]))

if __name__ == '__main__':
    main()