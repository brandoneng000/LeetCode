from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local = [[0] * (len(grid) - 2) for i in range(len(grid) - 2)]
        directions = [(-1, -1), (-1, 0), (-1, 1), \
                      (0, -1), (0, 0), (0, 1), \
                      (1, -1), (1, 0), (1, 1)]
        
        def get_max_local(row, col):
            row += 1
            col += 1
            res = 0
            for x, y in directions:
                res = max(res, grid[row + x][col + y])
            return res
            
        for i in range(len(max_local)):
            for j in range(len(max_local[0])):
                max_local[i][j] = get_max_local(i, j)
        
        return max_local
                

def main():
    sol = Solution()
    print(sol.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
    print(sol.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))

if __name__ == '__main__':
    main()