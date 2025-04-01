from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def make_palindrome(bits: List[int]):
            n = len(bits)
            flips = 0

            for i in range(n // 2):
                if bits[i] != bits[n - i - 1]:
                    flips += 1
            
            return flips

        row_flips = 0
        col_flips = 0

        for row in grid:
            row_flips += make_palindrome(row)

        for col in zip(*grid):
            col_flips += make_palindrome(col)
        
        return min(row_flips, col_flips)

        
def main():
    sol = Solution()
    print(sol.minFlips([[0,1],[1,1]]))
    print(sol.minFlips([[1,0,0],[0,0,0],[0,0,1]]))
    print(sol.minFlips([[0,1],[0,1],[0,0]]))
    print(sol.minFlips([[1],[0]]))

if __name__ == '__main__':
    main()