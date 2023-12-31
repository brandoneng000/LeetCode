from typing import List
from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def increase_rate(p: int, t: int):
            return (p + 1) / (t + 1) - p / t
        
        heap = []

        for p, t in classes:
            heappush(heap, (-increase_rate(p, t), p, t))

        for _ in range(extraStudents):
            inc, p, t = heappop(heap)
            heappush(heap, (-increase_rate(p + 1, t + 1), p + 1, t + 1))
        
        return sum(p / t for inc, p, t in heap) / len(heap)
        
def main():
    sol = Solution()
    print(sol.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
    print(sol.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))

if __name__ == '__main__':
    main()