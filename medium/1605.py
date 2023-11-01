from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res
        
def main():
    sol = Solution()
    print(sol.restoreMatrix(rowSum = [3,8], colSum = [4,7]))
    print(sol.restoreMatrix(rowSum = [5,7,10], colSum = [8,6,8]))

if __name__ == '__main__':
    main()