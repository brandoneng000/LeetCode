from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        cur = total = sum(nums)
        res = 0
        total /= 2
        heap = [-num for num in nums]
        heapify(heap)
        
        while cur > total:
            num = heappop(heap)
            cur -= -num / 2
            res += 1
            heappush(heap, num / 2)
        
        return res
        
def main():
    sol = Solution()
    print(sol.halveArray([5,19,8,1]))
    print(sol.halveArray([3,8,20]))

if __name__ == '__main__':
    main()