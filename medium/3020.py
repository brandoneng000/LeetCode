from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        one_count = count.get(1, 0)
        res = one_count if one_count % 2 else one_count - 1
        count.pop(1, None)

        for x in count:
            t = 0 

            while count[x] > 1:
                x *= x
                t += 2
            
            t += 1 if count[x] else -1
            res = max(res, t)
        
        return res

    # def maximumLength(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     visited = set()
    #     res = 1

    #     for num in sorted(count):
    #         if num in visited:
    #             continue
            
    #         if num == 1:
    #             res = max(res, count[1] if count[1] % 2 else count[1] - 1)
    #             continue

    #         if count[num] >= 2:
    #             cur = num
    #             cur_count = 1

    #             while count[cur * cur] >= 2:
    #                 cur_count += 1
    #                 cur *= cur
    #                 visited.add(cur)

    #             if count[cur * cur] == 1:
    #                 res = max(res, cur_count * 2 + 1)
    #             else:
    #                 res = max(res, (cur_count - 1) * 2 + 1)
            
    #     return res

        
def main():
    sol = Solution()
    print(sol.maximumLength([5,4,1,2,2]))
    print(sol.maximumLength([1,3,2,4]))

if __name__ == '__main__':
    main()