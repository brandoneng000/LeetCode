from typing import List
import collections

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = { (0, 0): 0 }

        for bits in strs:
            ones = bits.count('1')
            zeroes = len(bits) - ones
            new_dp = {}

            for (prev_zero, prev_one), val in dp.items():
                new_zero = prev_zero + zeroes
                new_one = prev_one + ones
                
                if new_zero <= m and new_one <= n:
                    if (new_zero, new_one) not in dp or dp[(new_zero, new_one)] < val + 1:
                        new_dp[(new_zero, new_one)] = val + 1
                
            dp.update(new_dp)
        
        return max(dp.values())

    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     dp = collections.defaultdict(lambda: collections.defaultdict(int))
        
    #     for bits in strs:
    #         zero = bits.count('0')
    #         one = len(bits) - zero

    #         for i in range(m, zero - 1, -1):
    #             for j in range(n, one - 1, -1):
    #                 dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        
    #     return dp[m][n]

def main():
    sol = Solution()
    print(sol.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
    print(sol.findMaxForm(strs = ["10","0","1"], m = 1, n = 1))

if __name__ == '__main__':
    main()