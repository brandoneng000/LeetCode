from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        negatives = 0
        lowest = float('inf')
        res = 0

        for i in range(m):
            for j in range(n):
                negatives += matrix[i][j] < 0
                res += abs(matrix[i][j])
                lowest = min(lowest, abs(matrix[i][j]))
        
        return res - (lowest * 2 if negatives & 1 else 0)
                
                
        
def main():
    sol = Solution()
    print(sol.maxMatrixSum([[1,-1],[-1,1]]))
    print(sol.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))

if __name__ == '__main__':
    main()