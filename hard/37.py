from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def set_up():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == '.':
                        uncertain.append((i, j))
                    else:
                        set_pos(i, j, ord(c) - ord('1'))

        def set_pos(i, j, x):
            x2 = 1 << x
            rows[i] |= x2
            cols[j] |= x2
            boxes[(i // 3) * 3 + j // 3] |= x2
        
        def solve(index):
            if index == len(uncertain):
                return True
            
            i, j = uncertain[index]
            index_box = (i // 3) * 3 + j // 3
            not_mask = ~(rows[i] | cols[j] | boxes[index_box]) & 0b111111111

            while not_mask:
                x = not_mask.bit_length() - 1
                bit = 1 << x
                board[i][j] = chr(ord('1') + x)
                rows[i] |= bit
                cols[j] |= bit
                boxes[index_box] |= bit

                if solve(index + 1):
                    return True
                board[i][j] = '.'
                rows[i] ^= bit
                cols[j] ^= bit
                boxes[index_box] ^= bit
                not_mask ^= bit
        
            return False

        uncertain = []
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        set_up()
        solve(0)
        
def main():
    sol = Solution()
    test = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    sol.solveSudoku(test)
    for row in test:
        print(row)

if __name__ == '__main__':
    main()