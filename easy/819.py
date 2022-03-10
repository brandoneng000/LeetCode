from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from re import sub
        from collections import Counter

        paragraph = sub('[^A-Za-z0-9 ]+', ' ', paragraph).lower().split()
        words = Counter(paragraph)
        
        for word in banned:
            if word in words:
                del words[word]

        return max(words, key=words.get)
        
def main():
    sol = Solution()
    print(sol.mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
    ))
    print(sol.mostCommonWord(
        "a, a, a, a, b,b,b,c, c", ["a"]
    ))

if __name__ == '__main__':
    main()