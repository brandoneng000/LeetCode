from typing import List
import collections

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        substrings = set()

        for i in range(len(strs)):
            if i not in substrings:
                for j in range(i + 1, len(strs)):
                    if self.if_substring(strs[j], strs[i]):
                        substrings.add(j)
                    if i not in substrings and self.if_substring(strs[i], strs[j]):
                        substrings.add(i)

                if i not in substrings:
                    return len(strs[i])
                

        return -1

    def if_substring(self, s1: str, s2:str):
        i1 = i2 = 0
        while i1 < len(s1) and i2 < len(s2):
            if s1[i1] == s2[i2]:
                i1 += 1
            i2 += 1
        
        return i1 == len(s1)


def main():
    sol = Solution()
    print(sol.findLUSlength(["aabbcc", "aabbcc","c"]))
    print(sol.findLUSlength(["aabbcc", "aabbcc","cb"]))
    print(sol.findLUSlength(["aba","cdc","eae"]))
    print(sol.findLUSlength(["aaa","aaa","aa"]))

if __name__ == '__main__':
    main()