from typing import List
from heapq import heappop, heapify

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        
        return res

    # def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    #     res = []
    #     heapify(nums)

    #     while nums:
    #         low = heappop(nums)
    #         mid = heappop(nums)
    #         high = heappop(nums)

    #         if high - low > k:
    #             return []
    #         res.append([low, mid, high])
        
    #     return res

    # def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    #     nums.sort()
    #     res = [[nums[i], nums[i + 1], nums[i + 2]] for i in range(0, len(nums), 3)]
        
    #     for group in res:
    #         if group[-1] - group[0] > k:
    #             return []

    #     return res

        
def main():
    sol = Solution()
    print(sol.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))
    print(sol.divideArray(nums = [1,3,3,2,7,3], k = 3))
    print(sol.divideArray(nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14))

if __name__ == '__main__':
    main()