from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for c in range(n)] for r in range(m)]
        
        for r,c in indices:
            for row in range(m):
                matrix[row][c] += 1
            for col in range(n):
                matrix[r][col] += 1
        
        return sum(matrix[i][j] % 2 for i in range(m) for j in range(n))


def main():
    sol = Solution()
    print(sol.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
    print(sol.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))

if __name__ == '__main__':
    main()