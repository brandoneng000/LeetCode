from typing import List
import collections

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        res = set()

        for word in words:
            even = "".join(sorted(word[::2]))
            odd = "".join(sorted(word[1::2]))
            res.add((even, odd))

        return len(res)
            


def main():
    sol = Solution()
    print(sol.numSpecialEquivGroups(words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
    print(sol.numSpecialEquivGroups(words = ["abc","acb","bac","bca","cab","cba"]))

if __name__ == '__main__':
    main()