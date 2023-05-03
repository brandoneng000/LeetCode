from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for row in matrix:
            for val in row:
                if len(heap) == k:
                    heapq.heappushpop(heap, -val)
                else:
                    heapq.heappush(heap, -val)
        
        return -heap[0]

def main():
    sol = Solution()
    print(sol.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
    print(sol.kthSmallest(matrix = [[-5]], k = 1))

if __name__ == '__main__':
    main()