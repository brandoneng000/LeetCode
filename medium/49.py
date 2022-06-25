from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            letters = "".join(sorted(word))
            # if letters in anagrams:
            #     anagrams[letters].append(word)
            # else:
            #     anagrams[letters] = [word]
            anagrams[letters] = anagrams.get(letters, []) + [word]
        
        return list(anagrams.values())

        
def main():
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == '__main__':
    main()