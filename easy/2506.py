from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        
        for i in range(len(words) - 1, -1, -1):  
            letters = set(words[i])
            for j in range(i - 1, -1, -1):
                if letters == set(words[j]):
                    res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.similarPairs(["aba","aabb","abcd","bac","aabc"]))
    print(sol.similarPairs(["aabb","ab","ba"]))
    print(sol.similarPairs(["nba","cba","dba"]))

if __name__ == '__main__':
    main()