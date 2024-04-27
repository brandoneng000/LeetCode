class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dp = [0] * n

        for k in range(len(key) - 1, -1, -1):
            next_dp = [float('inf')] * n

            for r in range(n):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dist = min(abs(r - i), len(ring) - abs(r - i))
                        next_dp[r] = min(next_dp[r], min_dist + 1 + dp[i])
            
            dp = next_dp
        
        return dp[0]



    # def findRotateSteps(self, ring: str, key: str) -> int:
    #     def helper(r: int, k: int):
    #         if k == len(key):
    #             return 0
    #         if (r, k) in cache:
    #             return cache[(r, k)]

    #         res = float('inf')

    #         for i, c in enumerate(ring):
    #             if c == key[k]:
    #                 min_dist = min(abs(r - i), len(ring) - abs(r - i))
    #                 res = min(res, min_dist + 1 + helper(i, k + 1))

    #         cache[(r, k)] = res
    #         return res
        
    #     cache = {}
    #     return helper(0, 0)

def main():
    sol = Solution()
    print(sol.findRotateSteps(ring = "godding", key = "gd"))
    print(sol.findRotateSteps(ring = "godding", key = "godding"))

if __name__ == '__main__':
    main()