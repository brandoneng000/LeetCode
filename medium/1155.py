import collections

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        dp = {}

        def helper(dice, target):
            if dice == 0:
                return 0 if target > 0 else 1
            
            if (dice, target) in dp:
                return dp[dice, target]

            res = 0
            for cur_sum in range(max(0, target - k), target):
                res += helper(dice - 1, cur_sum)
            dp[dice, target] = res

            return res
        
        return helper(n, target) % mod
    
def main():
    sol = Solution()
    print(sol.numRollsToTarget(n = 1, k = 6, target = 3))
    print(sol.numRollsToTarget(n = 2, k = 6, target = 7))
    print(sol.numRollsToTarget(n = 30, k = 30, target = 500))
    print(sol.numRollsToTarget(n = 30, k = 30, target = 30))

if __name__ == '__main__':
    main()