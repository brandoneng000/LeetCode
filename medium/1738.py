from typing import List
from heapq import heappush, heappop, heappushpop

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [[matrix[i][j] for j in range(n)] for i in range(m)]
        heap = []
        
        for i in range(m):
            for j in range(1, n):
                prefix[i][j] ^= prefix[i][j - 1]
        
        for i in range(n):
            for j in range(1, m):
                prefix[j][i] ^= prefix[j - 1][i]
        
        for i in range(m):
            for j in range(n):
                if len(heap) == k:
                    heappushpop(heap, prefix[i][j])
                else:
                    heappush(heap, prefix[i][j])
        
        return heap[0]

        
def main():
    sol = Solution()
    print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 1))
    print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 2))
    print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 3))
    print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 4))

if __name__ == '__main__':
    main()