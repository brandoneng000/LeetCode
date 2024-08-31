from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        pv = [-1] * n
        res = []

        for i in range(1, n):
            for j in range(i):
                if groups[i] == groups[j]:
                    continue
                if len(words[i]) != len(words[j]):
                    continue

                diff = sum(words[i][k] != words[j][k] for k in range(len(words[i])))

                if diff != 1:
                    continue

                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pv[i] = j
        
        wi = dp.index(max(dp))

        while wi != -1:
            res.append(words[wi])
            wi = pv[wi]

        res.reverse()
        return res
        
        

def main():
    sol = Solution()
    print(sol.getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2]))
    print(sol.getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4]))

if __name__ == '__main__':
    main()