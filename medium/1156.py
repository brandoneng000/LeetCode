from itertools import groupby
from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        groups = [[c, len(list(g))] for c, g in groupby(text)]
        text_count = Counter(text)

        res = max(min(k + 1, text_count[c]) for c, k in groups)
        
        for i in range(1, len(groups) - 1):
            if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
                res = max(res, min(groups[i - 1][1] + groups[i + 1][1] + 1, text_count[groups[i + 1][0]]))
        
        return res

def main():
    sol = Solution()
    print(sol.maxRepOpt1("ababa"))
    print(sol.maxRepOpt1("aaabaaa"))
    print(sol.maxRepOpt1("aaaaa"))

if __name__ == '__main__':
    main()