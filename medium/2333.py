from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        count = Counter(abs(n1 - n2) for n1, n2 in zip(nums1, nums2) if n1 != n2)
        heap = []
        k = k1 + k2

        for key in count:
            heappush(heap, [-key, count[key]])
        
        heappush(heap, [0, 0])
        
        while k and heap[0][0] != 0:
            num, c = heappop(heap)

            next_diff = heap[0][0] - num
            decrement = k // c
            remainder = k % c

            if decrement < next_diff:
                heappush(heap, [num + decrement, c - remainder])
                heappush(heap, [num + decrement + 1, remainder])
                break
    
            k -= min(next_diff, decrement) * c
            heap[0][1] += c

        
        return sum(num * num * c for num, c in heap)
        
        
def main():
    sol = Solution()
    print(sol.minSumSquareDiff(nums1 = [10,10,10,11,5], nums2 = [1,0,6,6,1], k1 = 11, k2 = 27))
    print(sol.minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0))
    print(sol.minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))

if __name__ == '__main__':
    main()