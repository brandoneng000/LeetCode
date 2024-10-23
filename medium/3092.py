from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        count = Counter()
        res = []

        for num, f in zip(nums, freq):
            count[num] = max(0, count[num] + f)
            heappush(heap, (-count[num], num))

            while heap[0][0] != -count[heap[0][1]]:
                prev_num, prev_freq = heappop(heap)

                if count[prev_num] > 0:
                    heappush(heap, (-count[prev_num], prev_num))
            
            if heap:
                res.append(-heap[0][0])
            else:
                res.append(0)
            
        return res
                
        
def main():
    sol = Solution()
    print(sol.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]))
    print(sol.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]))

if __name__ == '__main__':
    main()