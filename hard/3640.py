from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [-10**18 for _ in range(n)]
        dp1 = [-10**18 for _ in range(n)]
        dp2 = [-10**18 for _ in range(n)]
        dp3 = [-10**18 for _ in range(n)]
        dp0[0] = nums[0]
        res = -10**18

        for i in range(1, n):
            dp0[i] = nums[i]

            if nums[i] > nums[i - 1]:
                dp1[i] = max(dp0[i - 1], dp1[i - 1]) + nums[i]
                dp3[i] = max(dp2[i - 1], dp3[i - 1]) + nums[i]
            if nums[i] < nums[i - 1]:
                dp2[i] = max(dp1[i - 1], dp2[i - 1]) + nums[i]
            
            res = max(res, dp3[i])
        
        return res

    # def maxSumTrionic(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     left = [0] * n
    #     right = [0] * n

    #     for i in range(n):
    #         left[i] = nums[i]
    #         if i > 0 and nums[i - 1] < nums[i] and left[i - 1] > 0:
    #             left[i] += left[i - 1]
        
    #     for i in range(n - 1, -1, -1):
    #         right[i] = nums[i]
    #         if i + 1 < n and nums[i] < nums[i + 1] and right[i + 1] > 0:
    #             right[i] += right[i + 1]
        
    #     parts = []
    #     l, s = 0, nums[0]

    #     for i in range(1, n):
    #         if nums[i - 1] <= nums[i]:
    #             parts.append((l, i - 1, s))
    #             l, s = i, 0
    #         s += nums[i]
    #     parts.append((l, n - 1, s))

    #     res = -10 ** 26

    #     for p, q, s in parts:
    #         if p > 0 and q < n - 1 and nums[p - 1] < nums[p] and nums[q] < nums[q + 1] and p < q:
    #             res = max(res, left[p - 1] + s + right[q + 1])
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.maxSumTrionic([0,-2,-1,-3,0,2,-1]))
    print(sol.maxSumTrionic([1,4,2,7]))

if __name__ == '__main__':
    main()