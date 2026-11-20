from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        res = 0

        for x in nums:
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)
            res = max(res, dp[x], dp[x + 1])

        return res


def main():
    sol = Solution()
    print(sol.maxSelectedElements([2,1,5,1,1]))
    print(sol.maxSelectedElements([1,4,7,10]))

if __name__ == '__main__':
    main()