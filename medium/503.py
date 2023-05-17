from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            res[i % len(nums)] = -1 if not stack else nums[stack[-1]]
            stack.append(i % len(nums))

        return res
        
        # nums += nums
        # largest = max(nums)
        # res = [-float('inf')] * len(nums)
        # for i in range(len(nums) // 2):
        #     temp = i + 1
        #     while nums[i] >= nums[temp] and nums[i] != largest:
        #         temp += 1
        #     next_greater = nums[temp]
            
        #     if nums[i] == largest:
        #         res[i] = -1
        #     else:
        #         while temp >= i:
        #             res[temp] = next_greater
        #             temp -= 1
        
        # return res[:len(nums) // 2]

def main():
    sol = Solution()
    print(sol.nextGreaterElements([1,2,1]))
    print(sol.nextGreaterElements([1,2,3,4,3]))
    print(sol.nextGreaterElements([5,4,3,2,1]))

if __name__ == '__main__':
    main()