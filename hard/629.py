class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        prev = [0] * (k + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            cur = [0] * (k + 1)
            total = 0

            for j in range(k + 1):
                if j >= i:
                    total -= prev[j - i]

                total = (total + prev[j]) % mod
                cur[j] = total
            
            prev = cur
        
        return prev[k]


    # def kInversePairs(self, n: int, k: int) -> int:
    #     mod = 1000000007
    #     dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
    #     dp[0][0] = 1

    #     for i in range(1, n + 1):
    #         for j in range(k + 1):
                
    #             for pairs in range(i):
    #                 if j - pairs >= 0:
    #                     dp[i][j] += dp[i - 1][j - pairs]
        
    #     return dp[n][k] % mod
        

    # def kInversePairs(self, n: int, k: int) -> int:
    #     mod = 1000000007
    #     cache = {}

    #     def count_inverse_pairs(n: int, k: int):
    #         if n == 0:
    #             return 1 if k == 0 else 0
    #         if k < 0:
    #             return 0
            
    #         if (n, k) in cache:
    #             return cache[(n, k)]
            
    #         res = 0

    #         for i in range(n):
    #             res = (res + self.kInversePairs(n - 1, k - i)) % mod
        
    #         cache[(n, k)] = res
    #         return res
        
    #     return count_inverse_pairs(n, k)

def main():
    sol = Solution()
    print(sol.kInversePairs(n = 3, k = 2))
    print(sol.kInversePairs(n = 3, k = 0))
    print(sol.kInversePairs(n = 3, k = 1))

if __name__ == '__main__':
    main()