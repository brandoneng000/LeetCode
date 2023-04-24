from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        size_row = len(matrix)
        size_col = len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= size_row or c >= size_col:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
        
        helper(0, 0)
        return max(cache.values()) ** 2

def main():
    sol = Solution()
    print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(sol.maximalSquare([["0","1"],["1","0"]]))
    print(sol.maximalSquare([["0"]]))
    print(sol.maximalSquare([["1"]]))

if __name__ == '__main__':
    main()