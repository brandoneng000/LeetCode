from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        wiggle = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        count = 2 if wiggle[0] else 1
        prev = wiggle[0]
        for i in range(1, len(wiggle)):
            if (wiggle[i] > 0 and prev <= 0) or (wiggle[i] < 0 and prev >= 0):
                count += 1
                prev = wiggle[i]
                
        return count
        
        # if len(nums) < 2:
        #     return len(nums)
        
        # def helper(index: int, positive: bool):
        #     count = 0
        #     for i in range(index + 1, len(nums)):
        #         if (positive and nums[i] > nums[index]) or (not positive and nums[i] < nums[index]):
        #             count = max(count, helper(i, not positive) + 1)
            
        #     return count

        # return max(helper(0, True), helper(0, False)) + 1

def main():
    sol = Solution()
    print(sol.wiggleMaxLength([1,7,4,9,2,5]))
    print(sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(sol.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
    print(sol.wiggleMaxLength([1,1,3,4,5,6,7,8,9]))

if __name__ == '__main__':
    main()