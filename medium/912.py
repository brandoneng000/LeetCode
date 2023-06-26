from typing import List
import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []

        while nums:
            res.append(heapq.heappop(nums))
        
        return res
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     def merge(nums: List[int]):
    #         if len(nums) > 1:
    #             middle = len(nums) // 2
    #             l = nums[:middle]
    #             r = nums[middle:]

    #             merge(l)
    #             merge(r)

    #             i = j = k = 0

    #             while i < len(l) and j < len(r):
    #                 if l[i] <= r[j]:
    #                     nums[k] = l[i]
    #                     i += 1
    #                 else:
    #                     nums[k] = r[j]
    #                     j += 1
    #                 k += 1
                
    #             while i < len(l):
    #                 nums[k] = l[i]
    #                 i += 1
    #                 k += 1
                
    #             while j < len(r):
    #                 nums[k] = r[j]
    #                 j += 1
    #                 k += 1
    #     merge(nums)
    #     return nums

def main():
    sol = Solution()
    print(sol.sortArray([5,2,3,1]))
    print(sol.sortArray([5,1,1,2,0,0]))

if __name__ == '__main__':
    main()