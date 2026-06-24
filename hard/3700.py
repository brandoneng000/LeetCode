from itertools import accumulate

class Solution:
    MOD = 1_000_000_007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]

                if r == 0:
                    continue

                for j in range(m):
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD

        
        return res
    
    def pow_mul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)
            
            base = self.mul(base, base)
            exp >>= 1
        
        return res


    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m
        
        size = 2 * m
        u = [[0] * size for _ in range(size)]

        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1

            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = self.pow_mul(u, n - 1, dp)
        res = 0

        for i in range(size):
            res = (res + dp[0][i]) % self.MOD
        
        return res

        
def main():
    sol = Solution()
    print(sol.zigZagArrays(n = 3, l = 4, r = 5))
    print(sol.zigZagArrays(n = 3, l = 1, r = 3))

if __name__ == '__main__':
    main()