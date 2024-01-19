from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cur = matrix[0]

        for i in range(1, len(matrix)):
            next = matrix[i].copy()
            left = right = float('inf')

            for j in range(n):
                if j > 0:
                    left = cur[j - 1] + next[j]
                if j < n - 1:
                    right = cur[j + 1] + next[j]
                next[j] = min(cur[j] + next[j], left, right)
            cur = next
        
        return min(cur)
        

    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     for i in range(1, len(matrix)):
    #         left = float('inf')
    #         right = float('inf')
    #         for j in range(len(matrix)):
    #             if j > 0:
    #                 left = matrix[i - 1][j - 1] + matrix[i][j]
    #             if j < len(matrix[0]) - 1:
    #                 right = matrix[i - 1][j + 1] + matrix[i][j]
    #             matrix[i][j] = min(matrix[i - 1][j] + matrix[i][j], left, right)

    #     return min(matrix[-1])

def main():
    sol = Solution()
    print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(sol.minFallingPathSum([[-19,57],[-40,-5]]))

if __name__ == '__main__':
    main()