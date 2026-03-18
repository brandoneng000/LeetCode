from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        j = m - 1
        res = []

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        
        skip = j = 0

        for i, c in enumerate(word1):
            if j == m:
                break

            if word1[i] == word2[j] or skip == 0 and (j == m - 1 or i < last[j + 1]):
                skip += word1[i] != word2[j]
                res.append(i)
                j += 1
        
        return res if j == m else []
        
def main():
    sol = Solution()
    print(sol.validSequence(word1 = "vbcca", word2 = "abc"))
    print(sol.validSequence(word1 = "bacdc", word2 = "abc"))
    print(sol.validSequence(word1 = "aaaaaa", word2 = "aaabc"))

if __name__ == '__main__':
    main()