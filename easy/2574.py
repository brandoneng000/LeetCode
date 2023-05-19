from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        res = []

        for i in range(len(nums)):
            right -= nums[i]
            res.append(abs(left - right))
            left += nums[i]
        return res
        
        # left_sum = [0] * len(nums)
        # right_sum = [sum(nums)] * len(nums)

        # for i in range(len(nums)):
        #     right_sum[i] -= nums[i]
        #     for j in range(i + 1, len(nums)):
        #         left_sum[j] += nums[i]
        #         right_sum[j] -= nums[i]
        
        # return [abs(a - b) for a, b in zip(left_sum, right_sum)]



def main():
    sol = Solution()
    print(sol.leftRightDifference([10,4,8,3]))
    print(sol.leftRightDifference([1]))

if __name__ == '__main__':
    main()