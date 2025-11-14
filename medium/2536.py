from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        res = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else res[i - 1][j]
                x2 = 0 if j == 0 else res[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else res[i - 1][j - 1]
                res[i][j] = diff[i][j] + x1 + x2 - x3
        
        return res


    # def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
    #     res = [[0 for j in range(n + 1)] for i in range(n)]

    #     for r1, c1, r2, c2 in queries:
    #         for r in range(r1, r2 + 1):
    #             res[r][c1] += 1
    #             res[r][c2 + 1] -= 1
        
    #     for r in range(n):
    #         for c in range(1, n):
    #             res[r][c] += res[r][c - 1]
        
    #     return [res[i][:n] for i in range(n)]

        
def main():
    sol = Solution()
    print(sol.rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))
    print(sol.rangeAddQueries(n = 2, queries = [[0,0,1,1]]))

if __name__ == '__main__':
    main()