from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = collections.Counter(p)
        temp = collections.Counter(s[: len(p)])
        res = []

        if temp == p_count: res.append(0)
        for i in range(len(s) - len(p)):
            temp[s[i]] -= 1
            if i + len(p) < len(s):
                temp[s[i + len(p)]] = temp.get(s[i + len(p)], 0) + 1
                if temp == p_count:
                    res.append(i + 1)
        
        return res
    
        # p_count = collections.Counter(p)
        # res = []

        # for i in range(len(s) - len(p) + 1):
        #     if s[i] in p:
        #         temp = collections.Counter(s[i: i + len(p)])
        #         if temp == p_count:
        #             res.append(i)
        
        # return res

def main():
    sol = Solution()
    print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))
    print(sol.findAnagrams(s = "abab", p = "ab"))

if __name__ == '__main__':
    main()