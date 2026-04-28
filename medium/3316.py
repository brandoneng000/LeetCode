from typing import List

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        INF = 10 ** 33
        n, m = len(source), len(pattern)
        target = set(targetIndices)

        dp = [-INF] * m + [0]

        for i in range(n - 1, -1, -1):
            for j in range(m + 1):
                dp[j] += i in target

                if j < m and source[i] == pattern[j]:
                    dp[j] = max(dp[j], dp[j + 1])
        
        return dp[0]

        
def main():
    sol = Solution()
    print(sol.maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2]))
    print(sol.maxRemovals(source = "bcda", pattern = "d", targetIndices = [0,3]))
    print(sol.maxRemovals(source = "dda", pattern = "dda", targetIndices = [0,1,2]))
    print(sol.maxRemovals(source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]))

if __name__ == '__main__':
    main()