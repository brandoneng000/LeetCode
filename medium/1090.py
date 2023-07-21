from typing import List
import collections
import heapq

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        label_usage = collections.Counter()
        heap = []
        res = 0

        for val, label in zip(values, labels):
            heapq.heappush(heap, (-val, label))
        
        while heap and numWanted:
            val, label = heapq.heappop(heap)

            if label_usage[label] < useLimit:
                numWanted -= 1
                res += -val
                label_usage[label] += 1
        
        return res

def main():
    sol = Solution()
    print(sol.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1))
    print(sol.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2))
    print(sol.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1))

if __name__ == '__main__':
    main()