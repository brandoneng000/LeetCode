from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        return sum(not (set(word) - allowed_set) for word in words)


    # def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    #     res = 0

    #     for word in words:
    #         for letter in allowed:
    #             word = word.replace(letter, "")
            
    #         if not len(word):
    #             res += 1

    #     return res

def main():
    sol = Solution()
    print(sol.countConsistentStrings('ab', ["ad","bd","aaab","baa","badab"]))
    print(sol.countConsistentStrings('abc', ["a","b","c","ab","ac","bc","abc"]))
    print(sol.countConsistentStrings('cad', ["cc","acd","b","ba","bac","bad","ac","d"]))

if __name__ == '__main__':
    main()