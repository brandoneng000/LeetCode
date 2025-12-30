from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def helper(row: int, col: int):
            if grid[row + 1][col + 1] != 5:
                return False
            
            seen = set()

            for r in range(row, row + 3):
                for c in range(col, col+ 3):
                    if 0 < grid[r][c] < 10:
                        seen.add(grid[r][c])
            
            if len(seen) != 9:
                return False
            
            for r in range(row, row + 3):
                if grid[r][col] + grid[r][col + 1] + grid[r][col + 2] != 15:
                    return False
            
            for c in range(col, col + 3):
                if grid[row][c] + grid[row + 1][c] + grid[row + 2][c] != 15:
                    return False
                
            if grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15:
                return False
            
            if grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15:
                return False
            
            return True

        m, n = len(grid), len(grid[0])
        res = 0

        for row in range(m - 2):
            for col in range(n - 2):
                if helper(row, col):
                    res += 1
        
        return res

    # def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    #     def helper(grid: List[List[int]], row: int, col: int):
    #         sequence = "2943816729438167"
    #         sequence_reverse = "7618349276183492"

    #         border = []
    #         border_index = [0, 1, 2, 5, 8, 7, 6, 3]

    #         for i in border_index:
    #             num = grid[row + i // 3][col + (i % 3)]
    #             border.append(str(num))
            
    #         border_converted = ''.join(border)

    #         return (
    #             grid[row][col] % 2 == 0
    #             and (
    #                 sequence.find(border_converted) != -1
    #                 or sequence_reverse.find(border_converted) != -1
    #             )    
    #             and grid[row + 1][col + 1] == 5
    #         )

    #     m, n = len(grid), len(grid[0])
    #     res = 0

    #     for row in range(m - 2):
    #         for col in range(n - 2):
    #             if helper(grid, row, col):
    #                 res += 1
        
    #     return res


    # def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    #     if len(grid) < 3 or len(grid[0]) < 3:
    #         return 0
        
    #     num_set = set(range(1,10))
    #     res = 0
    #     for i in range(1, len(grid) - 1):
    #         for j in range(1, len(grid[0]) - 1):
    #             temp_set = set()
    #             for x in range(-1, 2):
    #                 for y in range(-1, 2):
    #                     temp_set.add(grid[i + x][j + y])
    #             if len(temp_set) == 9 and temp_set == num_set\
    #             and grid[i - 1][j] + grid[i + 1][j] \
    #             == grid[i][j - 1] + grid[i][j + 1] \
    #             == grid[i - 1][j - 1] + grid[i + 1][j + 1] \
    #             == grid[i - 1][j + 1] + grid[i + 1][j - 1] \
    #             and grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] \
    #             == grid[i][j - 1] + grid[i][j] + grid[i][j + 1] \
    #             == grid[i+ 1][j - 1] + grid[i+ 1][j] + grid[i+ 1][j + 1] \
    #             and grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1] \
    #             == grid[i - 1][j] + grid[i][j] + grid[i + 1][j] \
    #             == grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1]:
    #                 res += 1
        
    #     return res


def main():
    sol = Solution()
    print(sol.numMagicSquaresInside([[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]))
    print(sol.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
    print(sol.numMagicSquaresInside([[8]]))

if __name__ == '__main__':
    main()