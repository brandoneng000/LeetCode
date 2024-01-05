from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and all(words[i][0] == s[i] for i in range(len(s)))

        
def main():
    sol = Solution()
    print(sol.isAcronym(words = ["alice","bob","charlie"], s = "abc"))
    print(sol.isAcronym(words = ["an","apple"], s = "a"))
    print(sol.isAcronym(words = ["never","gonna","give","up","on","you"], s = "ngguoy"))

if __name__ == '__main__':
    main()