from typing import List
from collections import Counter

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        res = []

        for a, b in zip(A, B):
            set_a.add(a)
            set_b.add(b)
            res.append(len(set_a.intersection(set_b)))
        
        return res
        

    # def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    #     res = []
    #     seen = set()
    #     cur = 0

    #     for ab in zip(A, B):
    #         for num in ab:
    #             if num in seen:
    #                 cur += 1
    #             seen.add(num)
    #         res.append(cur)
        
    #     return res


    # def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    #     a_count = Counter()
    #     b_count = Counter()
    #     total = Counter()
    #     res = [0]

    #     for a, b in zip(A, B):
    #         a_count[a] += 1
    #         b_count[b] += 1
            
    #         if a == b:
    #             total[a] += 1
    #             res.append(res[-1] + 1)
    #         else:
    #             diff_a = min(a_count[a], b_count[a]) - total[a]
    #             diff_b = min(a_count[b], b_count[b]) - total[b]
    #             total[a] = min(a_count[a], b_count[a])
    #             total[b] = min(a_count[b], b_count[b])
    #             res.append(res[-1] + diff_a + diff_b)
            
    #     return res[1:]

def main():
    sol = Solution()
    print(sol.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))
    print(sol.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]))

if __name__ == '__main__':
    main()