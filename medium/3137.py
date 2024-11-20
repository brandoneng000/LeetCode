from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        count = Counter()
        res = n // k

        for i in range(0, n, k):
            count[word[i: i + k]] += 1
        
        return res - max(count.values())
        
def main():
    sol = Solution()
    print(sol.minimumOperationsToMakeKPeriodic(word = "leetcodeleet", k = 4))
    print(sol.minimumOperationsToMakeKPeriodic(word = "leetcoleet", k = 2))

if __name__ == '__main__':
    main()