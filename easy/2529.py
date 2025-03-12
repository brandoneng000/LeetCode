from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        negative = 0
        positive = n

        for i in range(n):
            if nums[i] < 0:
                negative += 1
            
            if nums[i] <= 0:
                positive -= 1
            else:
                break
        
        return max(negative, positive)


    # def maximumCount(self, nums: List[int]) -> int:
    #     if nums[0] == 0 and nums[-1] == 0: return 0
    #     left, right = 0, len(nums) - 1

    #     while left <= right:
    #         middle = (left + right) // 2

    #         if nums[middle] == 0:
    #             left = middle
    #             break
    #         elif nums[middle] > 0:
    #             right = middle - 1
    #         else:
    #             left = middle + 1
        
    #     positives = len(nums) - self.adjust_for_zero(nums, left, 1)
    #     negatives = self.adjust_for_zero(nums, left, -1)
    #     return max(positives, negatives)
        
    # def adjust_for_zero(self, nums: List[int], index: int, adjust: int):
    #     while 0 <= index < len(nums) and nums[index] == 0:
    #         index += adjust
    #     if index == len(nums):
    #         return index
    #     return index if nums[index] > 0 else index + 1

def main():
    sol = Solution()
    print(sol.maximumCount([-2,-1,-1,1,2,3]))
    print(sol.maximumCount([-3,-2,-1,0,0,1,2]))
    print(sol.maximumCount([5,20,66,1314]))
    print(sol.maximumCount([5,20]))
    print(sol.maximumCount([-1, -1]))

if __name__ == '__main__':
    main()