from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [[0 for j in range(n)] for i in range(m)]
        res = 0

        for r in range(m):
            for c in range(n):
                top = prefix[r - 1][c] if r > 0 else 0
                left = prefix[r][c - 1] if c > 0 else 0
                top_left = prefix[r - 1][c - 1] if min(r, c) > 0 else 0

                prefix[r][c] = matrix[r][c] + top + left - top_left
        
        for r1 in range(m):
            for r2 in range(r1, m):
                count = defaultdict(int)
                count[0] = 1

                for c in range(n):
                    top = prefix[r1 - 1][c] if r1 > 0 else 0
                    cur_sum = prefix[r2][c] - top
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        
        return res
    
    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     prefix = [[0 for j in range(n)] for i in range(m)]
    #     res = 0

    #     for r in range(m):
    #         for c in range(n):
    #             top = prefix[r - 1][c] if r > 0 else 0
    #             left = prefix[r][c - 1] if c > 0 else 0
    #             top_left = prefix[r - 1][c - 1] if min(r, c) > 0 else 0

    #             prefix[r][c] = matrix[r][c] + top + left - top_left
        
    #     for r1 in range(m):
    #         for r2 in range(r1, m):
    #             for c1 in range(n):
    #                 for c2 in range(c1, n):
    #                     top = prefix[r1 - 1][c2] if r1 > 0 else 0
    #                     left = prefix[r2][c1 - 1] if c1 > 0 else 0
    #                     top_left = prefix[r1 - 1][c1 - 1] if min(r1, c1) > 0 else 0

    #                     cur_sum = prefix[r2][c2] - top - left + top_left

    #                     if cur_sum == target:
    #                         res += 1
        
    #     return res
                

    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     prefix_row = [[0 for j in range(n + 1)] for i in range(m)]
    #     prefix_col = [[0 for j in range(n)] for i in range(m + 1)]
    #     res = 0

    #     for i in range(m):
    #         for j in range(1, n + 1):
    #             prefix_row[i][j] = prefix_row[i][j - 1] + matrix[i][j - 1]
        
    #     for j in range(n):
    #         for i in range(1, m + 1):
    #             prefix_col[i][j] = prefix_col[i - 1][j] + matrix[i - 1][j]
        
    #     for i in range(m):
    #         for j in range(n):
                
    #             for col in range(j + 1, n + 1):
    #                 cur = prefix_row[i][col] - prefix_row[i][j]
    #                 if cur == target:
    #                     res += 1
                
    #             for row in range(i + 2, m + 1):
    #                 cur = prefix_col[row][j] - prefix_col[i][j]
    #                 if cur == target:
    #                     res += 1
                
    #             for row in range(i + 2, m + 1):
    #                 cur = prefix_col[row][j] - prefix_col[i][j]
    #                 for col in range(j + 1, n):
    #                     cur += prefix_col[row][col] - prefix_col[i][col]
    #                     if cur == target:
    #                         res += 1
        
    #     return res



def main():
    sol = Solution()
    print(sol.numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))
    print(sol.numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))
    print(sol.numSubmatrixSumTarget(matrix = [[904]], target = 0))

if __name__ == '__main__':
    main()