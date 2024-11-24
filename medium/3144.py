from collections import Counter
from typing import List

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def is_balanced(count: List[int]):
            return len(set(count)) == 1

        n = len(s)
        dp = [n] * n

        for right in range(n):
            letters = Counter()

            for left in range(right, -1, -1):
                letters[s[left]] += 1

                if is_balanced(letters.values()):
                    dp[right] = min(dp[right], (1 + dp[left - 1]) if left > 0 else 1)
        
        return dp[n - 1]
        

def main():
    sol = Solution()
    print(sol.minimumSubstringsInPartition("fabccddg"))
    print(sol.minimumSubstringsInPartition("abababaccddb"))

if __name__ == '__main__':
    main()