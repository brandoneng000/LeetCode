class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mod = 1000000007
        count = 0
        dp[startRow][startColumn] = 1

        for move in range(1, maxMove + 1):
            temp = [[0 for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % mod
                    if j == n - 1:
                        count = (count + dp[i][j]) % mod
                    if i == 0:
                        count = (count + dp[i][j]) % mod
                    if j == 0:
                        count = (count + dp[i][j]) % mod
                    temp[i][j] = 0
                    for x, y in directions:
                        r, c = i + y, j + x
                        if 0 <= r < m and 0 <= c < n:
                            temp[i][j] = (temp[i][j] + dp[r][c]) % mod
            dp = temp
        
        return count
    
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # self.out_of_bounds = 0
        # self.cache = [[[-1 for i in range(maxMove + 1)] for j in range(n)] for k in range(m)]
        # mod = 1000000007

        # def helper(pos_x: int, pos_y: int, moves: int):
        #     if pos_x < 0 or pos_y < 0 or pos_x == m or pos_y == n:
        #         return 1
        #     if moves == 0:
        #         return 0
        #     if self.cache[pos_x][pos_y][moves] >= 0:
        #         return self.cache[pos_x][pos_y][moves]
            
        #     total = 0
        #     for x, y in directions:
        #         r, c = pos_x + x, pos_y + y
        #         total += helper(r, c, moves - 1) % mod
        #     self.cache[pos_x][pos_y][moves] = total % mod
        #     return self.cache[pos_x][pos_y][moves]
        
        # return helper(startRow, startColumn, maxMove)



def main():
    sol = Solution()
    print(sol.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
    print(sol.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
    print(sol.findPaths(m = 1, n = 2, maxMove = 3, startRow = 0, startColumn = 0))

if __name__ == '__main__':
    main()