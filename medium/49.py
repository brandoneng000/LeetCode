from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            letters = "".join(sorted(word))
            anagrams[letters].append(word)
        
        return [anagrams[letters] for letters in anagrams]

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagrams = {}

    #     for word in strs:
    #         letters = "".join(sorted(word))
    #         # if letters in anagrams:
    #         #     anagrams[letters].append(word)
    #         # else:
    #         #     anagrams[letters] = [word]
    #         anagrams[letters] = anagrams.get(letters, []) + [word]
        
    #     return list(anagrams.values())

        
def main():
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))

if __name__ == '__main__':
    main()