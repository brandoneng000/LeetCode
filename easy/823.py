from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1000000007
        
        n = len(arr)
        dp = [1] * n

        arr.sort()
        indexes = { val: i for i, val in enumerate(arr) }
        for i in range(n):
            for j in range(i):
                div, r = divmod(arr[i], arr[j])
                if r == 0 and div in indexes:
                    dp[i] += dp[j] * dp[indexes[div]]
                    dp[i] %= mod
        
        return sum(dp) % mod


def main():
    sol = Solution()
    print(sol.numFactoredBinaryTrees([2,4]))
    # [2], [4], [8], [4,2,2], [8,4,2], [8,2,4], [8,4,2,2,2], [8,2,4,2,2]
    #  1    2    1
    print(sol.numFactoredBinaryTrees([2,4,8]))
    print(sol.numFactoredBinaryTrees([2,4,5,10]))

if __name__ == '__main__':
    main()