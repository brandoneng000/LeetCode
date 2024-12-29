from typing import List
from collections import defaultdict, Counter

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        def backtrack(index: int, target_index: int, target: str, dp: List[List[int]], letters: defaultdict):
            if target_index == n:
                return 1
            
            if index == m or m - index < n - target_index:
                return 0
            
            if dp[index][target_index] != -1:
                return dp[index][target_index]
            
            count = 0
            count += backtrack(index + 1, target_index, target, dp, letters)
            count += letters[index][target[target_index]] * backtrack(index + 1, target_index + 1, target, dp, letters)

            dp[index][target_index] = count % mod
            return dp[index][target_index]


        mod = 1000000007
        n, m = len(target), len(words[0])
        letters = defaultdict(Counter)
        dp = [[-1] * n for _ in range(m)]

        for word in words:
            for i in range(m):
                letters[i][word[i]] += 1

        return backtrack(0, 0, target, dp, letters)
        

        
def main():
    sol = Solution()
    print(sol.numWays(words = ["acca","bbbb","caca"], target = "aba"))
    print(sol.numWays(words = ["abba","baab"], target = "bab"))

if __name__ == '__main__':
    main()