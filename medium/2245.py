from typing import List

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def helper(num: int):
            two, five = 0, 0

            while num % 2 == 0:
                num //= 2
                two += 1
            while num % 5 == 0:
                num //= 5
                five += 1
            
            return [two, five]
        
        m, n = len(grid), len(grid[0])
        top = [[[0, 0] for j in range(n)] for i in range(m)]
        left = [[[0, 0] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    left[i][j] = helper(grid[i][j])
                else:
                    two, five = helper(grid[i][j])
                    left[i][j][0] = left[i][j - 1][0] + two
                    left[i][j][1] = left[i][j - 1][1] + five
        
        for j in range(n):
            for i in range(m):
                if i == 0:
                    top[i][j] = helper(grid[i][j])
                else:
                    two, five = helper(grid[i][j])
                    top[i][j][0] = top[i - 1][j][0] + two
                    top[i][j][1] = top[i - 1][j][1] + five

        res = 0
        for i in range(m):
            for j in range(n):
                a, b = top[m - 1][j]
                d, e = left[i][n - 1]

                x, y = helper(grid[i][j])

                a1, b1 = top[i][j]
                a2, b2 = left[i][j]
                temp = [a1 + a2 - x, b1 + b2 - y]
                res = max(res, min(temp))
                temp = [d - a2 + a1, e - b2 + b1]
                res = max(res, min(temp))             
                temp = [a - a1 + a2, b - b1 + b2]
                res = max(res, min(temp))
                temp = [a + d - a1 - a2 + x, b + e - b1 - b2 + y]
                res = max(res, min(temp))
        
        return res

        
        
def main():
    sol = Solution()
    print(sol.maxTrailingZeros([[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]))
    print(sol.maxTrailingZeros([[4,3,2],[7,6,1],[8,8,8]]))

if __name__ == '__main__':
    main()