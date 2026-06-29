from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for p in patterns:
            if p in word:
                res += 1
        
        return res

    # def numOfStrings(self, patterns: List[str], word: str) -> int:
    #     return sum(pattern in word for pattern in patterns)

def main():
    sol = Solution()
    print(sol.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc"))
    print(sol.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb"))
    print(sol.numOfStrings(patterns = ["a","a","a"], word = "ab"))

if __name__ == '__main__':
    main()