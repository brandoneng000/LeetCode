from typing import List
import collections

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = []
        zero = False
        
        for num in nums:
            if num == 1:
                cur.append(1)
                res = max(res, len(cur) - (1 if zero else 0))
                continue
            if cur and zero and num == 0:
                index = cur.index(0)
                cur = cur[index + 1:]
                cur.append(0)
            elif not cur or not zero and num == 0:
                cur.append(0)
                zero = True
        
        return res if zero else res - 1
            


def main():
    sol = Solution()
    print(sol.longestSubarray([1,1,0,1]))
    print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
    print(sol.longestSubarray([1,1,1]))

if __name__ == '__main__':
    main()