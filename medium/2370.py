from typing import List

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * (ord('z') + 1)

        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k: i + k + 1]) + 1
        
        return max(dp)



def main():
    sol = Solution()
    print(sol.longestIdealString(s = "acfgbd", k = 2))
    print(sol.longestIdealString(s = "abcd", k = 3))

if __name__ == '__main__':
    main()