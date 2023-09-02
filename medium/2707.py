from typing import List
from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dict_set = set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            
            res = dp(start + 1) + 1

            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dict_set:
                    res = min(res, dp(end + 1))
            
            return res
        
        return dp(0)

        
def main():
    sol = Solution()
    print(sol.minExtraChar(s = "leetcode", dictionary = ["leet","code","leetcode"]))
    print(sol.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
    print(sol.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))

if __name__ == '__main__':
    main()