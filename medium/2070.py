from typing import List
from bisect import bisect_right
from collections import defaultdict

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items_dict = defaultdict(int)
        items.sort()
        res = []
        cur = 0

        for p, b in items:
            cur = max(cur, b)
            items_dict[p] = cur
        
        items_dict[0] = 0
        keys = sorted(items_dict.keys())

        for q in queries:
            index = bisect_right(keys, q) - 1
            res.append(items_dict[keys[index]])

        return res


    # def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    #     items.append([0, 0])
    #     items.sort()
    #     n = len(items)
    #     res = []

    #     for i in range(1, n):
    #         items[i][1] = max(items[i][1], items[i - 1][1])

    #     for q in queries:
    #         index = bisect_right(items, q, key=lambda x: x[0])
    #         res.append(items[index - 1][1])
        
    #     return res
        


        
def main():
    sol = Solution()
    print(sol.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))
    print(sol.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))
    print(sol.maximumBeauty(items = [[10,1000]], queries = [5]))

if __name__ == '__main__':
    main()