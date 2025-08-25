from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        row = col = 0

        for _ in range(m * n):
            res.append(mat[row][col])

            if (row + col) % 2 == 0:
                if col == n - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        
        return res

    # def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    #     if not mat or not mat[0]:
    #         return []
        
    #     row, col = 0, 0
    #     direction = 1
    #     res = []
    #     while row < len(mat) and col < len(mat[0]):
    #         res.append(mat[row][col])
    #         next_row = row + (-1 if direction == 1 else 1)
    #         next_col = col + (1 if direction == 1 else -1)

    #         if next_row < 0 or next_row == len(mat) or next_col < 0 or next_col == len(mat[0]):
    #             if direction:
    #                 row += (col == len(mat[0]) - 1)
    #                 col += (col < len(mat[0]) - 1)
    #             else:
    #                 col += (row == len(mat) - 1)
    #                 row += (row < len(mat) - 1)
                
    #             direction = 1 - direction
    #         else:
    #             row = next_row
    #             col = next_col
        
    #     return res

def main():
    sol = Solution()
    print(sol.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder(mat = [[1,2],[3,4]]))

if __name__ == '__main__':
    main()