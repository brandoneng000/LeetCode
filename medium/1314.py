from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = [[0 for j in range(n)] for i in range(m)]


        for r in range(1, m + 1):
            for c in range(1, n + 1):
                prefix[r][c] = mat[r - 1][c - 1] + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1]
        
        for r in range(m):
            for c in range(n):
                r1 = max(0, r - k) + 1
                c1 = max(0, c - k) + 1
                r2 = min(m - 1, r + k) + 1
                c2 = min(n - 1, c + k) + 1
                # print(prefix[r2][c2], prefix[r2][c1 - 1], prefix[r1 - 1][c2], prefix[r1 - 1][c1 - 1])
                res[r][c] = prefix[r2][c2] - prefix[r2][c1 - 1] - prefix[r1 - 1][c2] + prefix[r1 - 1][c1 - 1]

        return res


    # def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
    #     m, n = len(mat), len(mat[0])
    #     res = [[0 for j in range(n)] for i in range(m)]

    #     for i in range(m):
    #         for j in range(n):
    #             cur = 0
    #             for r in range(i - k, i + k + 1):
    #                 for c in range(j - k, j + k + 1):
    #                     if 0 <= r < m and 0 <= c < n:
    #                         cur += mat[r][c]
                
    #             res[i][j] = cur
        
    #     return res

def main():
    sol = Solution()
    print(sol.matrixBlockSum(mat = [[5,6],[8,9]], k = 1))
    print(sol.matrixBlockSum(mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]], k = 3))
    print(sol.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
    print(sol.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2))

if __name__ == '__main__':
    main()