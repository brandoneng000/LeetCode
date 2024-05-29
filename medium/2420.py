from typing import List
from collections import deque

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        forward = [False] * n
        stack = []

        for i in range(n):
            if len(stack) >= k:
                forward[i] = True
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] <= stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]
        
        stack = []
        for i in range(n - 1, -1, -1):
            if len(stack) >= k and forward[i]:
                res.append(i)
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] <= stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]
        
        return res[::-1]
            
    
    # def goodIndices(self, nums: List[int], k: int) -> List[int]:
    #     def non_increasing(left: List[int]):
    #         for i in range(1, len(left)):
    #             if left[i - 1] < left[i]:
    #                 return False
            
    #         return True
        
    #     def non_decreasing(right: List[int]):
    #         for i in range(1, len(right)):
    #             if right[i - 1] > right[i]:
    #                 return False
            
    #         return True

    #     n = len(nums)
    #     left = deque(nums[:k])
    #     right = deque(nums[k + 1: k + k + 1])
    #     res = []

    #     for i in range(k, n - k):
    #         if non_increasing(left) and non_decreasing(right):
    #             res.append(i)
            
    #         left.popleft()
    #         left.append(nums[i])
    #         right.popleft()
    #         if i + k + 1 < n:
    #             right.append(nums[i + k + 1])
        
    #     return res

        

def main():
    sol = Solution()
    print(sol.goodIndices(nums = [440043,276285,336957], k = 1))
    print(sol.goodIndices(nums = [2,1,1,1,3,4,1], k = 2))
    print(sol.goodIndices(nums = [2,1,1,2], k = 2))

if __name__ == '__main__':
    main()