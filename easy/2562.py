from typing import List
import collections

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = 0

        while left <= right:
            if left == right:
                res += nums[left]
            else:
                res += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        
        return res
        
        # nums = collections.deque(nums)

        # res = 0
        # while nums:
        #     if len(nums) > 1:
        #         nums1 = nums.popleft()
        #         nums2 = nums.pop()
        #         temp = 10
        #         while temp <= nums2:
        #             temp *= 10
        #         nums1 *= temp
        #         res += nums1 + nums2
        #     else:
        #         res += nums.pop()
        
        # return res

        # nums = collections.deque(nums)

        # res = 0
        # while nums:
        #     if len(nums) > 1:
        #         res += int(str(nums.popleft()) + str(nums.pop()))
        #     else:
        #         res += nums.pop()
        
        # return res
                
def main():
    sol = Solution()
    print(sol.findTheArrayConcVal([7,52,2,4]))
    print(sol.findTheArrayConcVal([5,14,13,8,12]))
    print(sol.findTheArrayConcVal([1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28]))

if __name__ == '__main__':
    main()