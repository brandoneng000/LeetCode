from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        num_set = set(range(1,10))
        res = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                temp_set = set()
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        temp_set.add(grid[i + x][j + y])
                if len(temp_set) == 9 and temp_set == num_set\
                and grid[i - 1][j] + grid[i + 1][j] \
                == grid[i][j - 1] + grid[i][j + 1] \
                == grid[i - 1][j - 1] + grid[i + 1][j + 1] \
                == grid[i - 1][j + 1] + grid[i + 1][j - 1] \
                and grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] \
                == grid[i][j - 1] + grid[i][j] + grid[i][j + 1] \
                == grid[i+ 1][j - 1] + grid[i+ 1][j] + grid[i+ 1][j + 1] \
                and grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1] \
                == grid[i - 1][j] + grid[i][j] + grid[i + 1][j] \
                == grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1]:
                    res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
    print(sol.numMagicSquaresInside([[8]]))

if __name__ == '__main__':
    main()