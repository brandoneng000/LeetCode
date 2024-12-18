from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[::]
        heap = [[num, i] for i, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            num, i = heappop(heap)
            res[i] = num * multiplier
            heappush(heap, [res[i], i])

        return res
        

def main():
    sol = Solution()
    print(sol.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
    print(sol.getFinalState(nums = [1,2], k = 3, multiplier = 4))

if __name__ == '__main__':
    main()