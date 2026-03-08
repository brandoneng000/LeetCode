from typing import List
from collections import Counter

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = Counter(message)
        res = 0

        for word in set(bannedWords):
            res += count[word]

            if res >= 2:
                break
        
        return res >= 2
        
def main():
    sol = Solution()
    print(sol.reportSpam(message = ["hello","world","leetcode"], bannedWords = ["world","hello"]))
    print(sol.reportSpam(message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]))

if __name__ == '__main__':
    main()