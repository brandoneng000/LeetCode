from typing import List
import collections

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for bits in strs:
            zero = bits.count('0')
            one = len(bits) - zero

            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        
        return dp[m][n]

def main():
    sol = Solution()
    print(sol.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
    print(sol.findMaxForm(strs = ["10","0","1"], m = 1, n = 1))

if __name__ == '__main__':
    main()