from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1000000007
        
        def multiply_matrices(A, B):
            rows_A, cols_A, cols_B = len(A), len(B), len(B[0])
            res = [[0] * cols_B for _ in range(rows_A)]

            for i in range(rows_A):
                for j in range(cols_B):
                    temp = 0

                    for k in range(cols_A):
                        temp += A[i][k] * B[k][j]
                    
                    res[i][j] = temp % mod
            
            return res
        
        def power_matrix(matrix, exponent):
            n = len(matrix)
            res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

            while exponent > 0:
                if exponent & 1:
                    res = multiply_matrices(res, matrix)

                matrix = multiply_matrices(matrix, matrix)
                exponent >>= 1
            
            return res
        
        transform = [[0] * 26 for _ in range(26)]

        for i in range(26):
            for shift in range(nums[i]):
                transform[i][(i + 1 + shift) % 26] += 1

        transform = power_matrix(transform, t)
        freq = [[0] * 26]

        for ch in s:
            freq[0][ord(ch) - ord('a')] += 1

        freq = multiply_matrices(freq, transform)

        return sum(freq[0]) % mod
        
def main():
    sol = Solution()
    print(sol.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(sol.lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))

if __name__ == '__main__':
    main()