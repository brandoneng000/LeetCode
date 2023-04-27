from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Live cell with <2 living neighbors -> die
        Live cell with 2 or 3 living neighbors -> live
        Live cell with >3 living neighbors -> die
        Dead cell with 3 live neighbors -> live
        """
        # directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        # generation = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        # def check_surrounding(row, col):
        #     res = 0
        #     for dx, dy in directions:
        #         x = row + dx
        #         y = col + dy
        #         if 0 <= x < len(board) and 0 <= y < len(board[0]):
        #             res += board[x][y]
            
        #     return res

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         generation[i][j] = check_surrounding(i, j)

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j]:
        #             if generation[i][j] < 2 or generation[i][j] > 3:
        #                 board[i][j] = 0
        #         else:
        #             if generation[i][j] == 3:
        #                 board[i][j] = 1
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        generation = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        def check_surrounding(row, col):
            for dx, dy in directions:
                x = row + dx
                y = col + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    generation[x][y] += board[row][col]

        for i in range(len(board)):
            for j in range(len(board[0])):
                check_surrounding(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    if generation[i][j] < 2 or generation[i][j] > 3:
                        board[i][j] = 0
                else:
                    if generation[i][j] == 3:
                        board[i][j] = 1

def main():
    sol = Solution()
    temp = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol.gameOfLife(temp)
    print(temp)
    temp = [[1,1],[1,0]]
    sol.gameOfLife(temp)
    print(temp)

if __name__ == '__main__':
    main()