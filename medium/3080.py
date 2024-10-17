from typing import List
from heapq import heappush, heappop

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = [0] * n
        marked = set()
        heap = []
        total = 0

        for i, num in enumerate(nums):
            heappush(heap, (num, i))
            total += num
        
        for i, (index, k) in enumerate(queries):
            if index not in marked:
                total -= nums[index]

            marked.add(index)
            
            while heap and k:
                cur, j = heappop(heap)

                if j in marked:
                    continue
                
                marked.add(j)
                total -= cur
                k -= 1

            res[i] = total

            if not heap:
                break

        return res
        
def main():
    sol = Solution()
    print(sol.unmarkedSumArray(nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]))
    print(sol.unmarkedSumArray(nums = [1,4,2,3], queries = [[0,1]]))

if __name__ == '__main__':
    main()