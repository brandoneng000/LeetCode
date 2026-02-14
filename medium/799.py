class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(1, 102)]
        dp[0][0] = poured

        for r in range(query_row):
            for c in range(r + 1):
                if dp[r][c] > 1:
                    excess = dp[r][c] - 1
                    dp[r + 1][c] += excess / 2
                    dp[r + 1][c + 1] += excess / 2
                    dp[r][c] = 1
        
        return min(1, dp[query_row][query_glass])


    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    #     cups = {}

    #     for i in range(query_row + 2):
    #         cups[i] = [0] * (i + 1)
        
    #     cups[0][0] = poured
    #     for r in range(query_row + 1):
    #         for c in range(r + 1):
    #             q = (cups[r][c] - 1.0) / 2.0
    #             if q > 0:
    #                 cups[r + 1][c] += q
    #                 cups[r + 1][c + 1] += q
        
    #     return min(1, cups[query_row][query_glass])

def main():
    sol = Solution()
    print(sol.champagneTower(poured = 1, query_row = 3, query_glass = 3))
    print(sol.champagneTower(poured = 1, query_row = 1, query_glass = 1))
    print(sol.champagneTower(poured = 2, query_row = 1, query_glass = 1))
    print(sol.champagneTower(poured = 1, query_row = 4, query_glass = 2))
    print(sol.champagneTower(poured = 100000009, query_row = 33, query_glass = 17))

if __name__ == '__main__':
    main()