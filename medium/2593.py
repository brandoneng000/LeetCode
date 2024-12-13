from typing import List
from heapq import heappush, heappop

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        sorted_nums = sorted([(num, index) for index, num in enumerate(nums)])
        res = 0

        for i in range(n):
            num, index = sorted_nums[i]

            if not marked[index]:
                res += num
                marked[index] = True
                if index + 1 < n:
                    marked[index + 1] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
            
        return res

    # def findScore(self, nums: List[int]) -> int:
    #     marked = set()
    #     res = 0
    #     heap = []

    #     for index, num in enumerate(nums):
    #         heappush(heap, (num, index))

    #     while heap:
    #         num, index = heappop(heap)

    #         if index in marked:
    #             continue

    #         res += num
    #         marked.add(index)
    #         marked.add(index + 1)
    #         marked.add(index - 1)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.findScore([2,1,3,4,5,2]))
    print(sol.findScore([2,3,5,1,3,2]))

if __name__ == '__main__':
    main()