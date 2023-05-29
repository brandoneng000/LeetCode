class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        board = [[0 for i in range(n)] for j in range(n)]
        board[row][column] = 1
        size = 8 ** k

        while k:
            k -= 1
            next_board = [[0 for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    for r, c in moves:
                        row = i + r
                        col = j + c
                        if 0 <= row < n and 0 <= col < n:
                            next_board[i][j] += board[row][col]
            
            board = next_board

        return sum(sum(board, [])) / size

    # def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    #     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    #     pos = [(row, column)]
    #     size = 8 ** k

    #     while k:
    #         k -= 1
    #         temp = []
    #         while pos:
    #             cur_row, cur_col = pos.pop()
    #             for move_row, move_col in moves:
    #                 new_row = cur_row + move_row
    #                 new_col = cur_col + move_col
    #                 if 0 <= new_row < n and 0 <= new_col < n:
    #                     temp.append((new_row, new_col))
    #         pos = temp
        
    #     return len(pos) / size

def main():
    sol = Solution()
    print(sol.knightProbability(n = 3, k = 2, row = 0, column = 0))
    print(sol.knightProbability(n = 1, k = 0, row = 0, column = 0))

if __name__ == '__main__':
    main()