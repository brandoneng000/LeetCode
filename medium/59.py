from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for r in range(n)] for c in range(n)]
        row, col, row_dir, col_dir = 0, 0, 0, 1

        for val in range(1, n * n + 1):
            result[row][col] = val
            if result[(row + row_dir) % n][(col + col_dir) % n]:
                row_dir, col_dir = col_dir, -row_dir
            row += row_dir
            col += col_dir
            
        return result



def main():
    sol = Solution()
    print(sol.generateMatrix(3))
    print(sol.generateMatrix(1))

if __name__ == '__main__':
    main()