from typing import List
from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_deq = deque(nums)
        res = []

        while nums_deq:
            if abs(nums_deq[0]) > abs(nums_deq[-1]):
                res.append(nums_deq[0] * nums_deq[0])
                nums_deq.popleft()
            else:
                res.append(nums_deq[-1] * nums_deq[-1])
                nums_deq.pop()
        
        return res[::-1]

    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     n = len(nums)

    #     neg_index = -1
        
    #     while neg_index < n - 1 and nums[neg_index + 1] < 0:
    #         neg_index += 1
        
    #     pos_index = neg_index + 1
    #     res = []

    #     while neg_index > -1 or pos_index < n:
    #         if neg_index > -1 and pos_index < n:
    #             if abs(nums[neg_index]) < nums[pos_index]:
    #                 res.append(nums[neg_index] * nums[neg_index])
    #                 neg_index -= 1
    #             else:
    #                 res.append(nums[pos_index] * nums[pos_index])
    #                 pos_index += 1
    #         elif neg_index > -1:
    #             res.append(nums[neg_index] * nums[neg_index])
    #             neg_index -= 1
    #         else:
    #             res.append(nums[pos_index] * nums[pos_index])
    #             pos_index += 1
        
    #     return res
                

    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     if len(nums) == 1:
    #         return [nums[0] ** 2]
        
    #     result = []
    #     index = 0

    #     while index < len(nums) and nums[index] < 0:
    #         index += 1
        
    #     negatives = nums[:index]
    #     positives = nums[index:]
    #     negatives = negatives[::-1]

    #     pos_index = 0
    #     neg_index = 0

    #     while pos_index < len(positives) or neg_index < len(negatives):
    #         if pos_index == len(positives):
    #             result.append(negatives[neg_index] ** 2)
    #             neg_index += 1
    #         elif neg_index == len(negatives):
    #             result.append(positives[pos_index] ** 2)
    #             pos_index += 1
    #         else:
    #             if abs(negatives[neg_index]) > positives[pos_index]:
    #                 result.append(positives[pos_index] ** 2)
    #                 pos_index += 1
    #             else:
    #                 result.append(negatives[neg_index] ** 2)
    #                 neg_index += 1
        
    #     return result
        

def main():
    sol = Solution()
    print(sol.sortedSquares([-4,-1,0,3,10]))
    print(sol.sortedSquares([-7,-3,2,3,11]))
    print(sol.sortedSquares([2]))
    print(sol.sortedSquares([-4, -4, -3]))

if __name__ == '__main__':
    main()