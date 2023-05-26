from typing import List
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            middle = (left + right) // 2
            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle
        
        return arr[left: left + k]
        
        
        # heap = []
        
        # for n in arr:
        #     heapq.heappush(heap, (abs(n - x), n))
        
        # closest = heapq.nsmallest(k, heap)
        # return [num[1] for num in sorted(closest, key=lambda x: x[1])]
    
def main():
    sol = Solution()
    print(sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
    print(sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))

if __name__ == '__main__':
    main()