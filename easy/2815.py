from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_digit = { nums[i]: int(max(str(nums[i]))) for i in range(n) }
        res = -1
        
        for i in range(n):
            for j in range(i + 1, n):
                if max_digit[nums[i]] == max_digit[nums[j]]:
                    res = max(res, nums[i] + nums[j])

        return res

def main():
    sol = Solution()
    print(sol.maxSum([51,71,17,24,42]))
    print(sol.maxSum([1,2,3,4]))

if __name__ == '__main__':
    main()