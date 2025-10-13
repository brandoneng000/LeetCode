from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        res = [words[0]]

        for i in range(1, n):
            if sorted(words[i]) == sorted(res[-1]):
                continue
            res.append(words[i])
        
        return res

    # def removeAnagrams(self, words: List[str]) -> List[str]:
    #     result = []
    #     prev = tuple()

    #     for word in words:
    #         key = tuple(sorted(word))
    #         if key != prev:
    #             prev = key
    #             result.append(word)
            
    #     return result
        
def main():
    sol = Solution()
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd","abab"]))
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd","bbaa"]))
    print(sol.removeAnagrams(["a","b","c","d","e"]))

if __name__ == '__main__':
    main()