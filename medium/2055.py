from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i, c in enumerate(s) if c == '|']
        res = []

        for left, right in queries:
            i = bisect_left(candles, left)
            j = bisect_right(candles, right) - 1
            res.append((candles[j] - candles[i]) - (j - i) if i < j else 0)
        
        return res


def main():
    sol = Solution()
    print(sol.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))
    print(sol.platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))

if __name__ == '__main__':
    main()