from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = tuple()

        for word in words:
            key = tuple(sorted(word))
            if key != prev:
                prev = key
                result.append(word)
            
        return result
        
def main():
    sol = Solution()
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd","abab"]))

if __name__ == '__main__':
    main()