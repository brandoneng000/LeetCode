from typing import List

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        INF = 10 ** 33
        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word

        n = len(target)
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            node = trie
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1 + dp[j + 1])
            
        return dp[0] if dp[0] < INF else -1

        
def main():
    sol = Solution()
    print(sol.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc"))
    print(sol.minValidStrings(words = ["abababab","ab"], target = "ababaababa"))
    print(sol.minValidStrings(words = ["abcdef"], target = "xyz"))

if __name__ == '__main__':
    main()