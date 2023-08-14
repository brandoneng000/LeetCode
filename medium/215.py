from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]


def main():
    sol = Solution()
    print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    print(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

if __name__ == '__main__':
    main()