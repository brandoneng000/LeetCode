from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        res = n + 1
        total = 0

        dp = [n] * (n + 1)
        left = 0

        for right, x in enumerate(arr):
            total += x

            while total > target:
                total -= arr[left]
                left += 1

            dp[right + 1] = dp[right]

            if total == target:
                res = min(res, right - left + 1 + dp[left])
                dp[right + 1] = min(dp[right], right - left + 1)

        return -1 if res == n + 1 else res

    # def minSumOfLengths(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     prefix = [float('inf')] * n
    #     res = float('inf')
    #     left = cur = 0

    #     for right in range(n):
    #         cur += arr[right]
    #         while cur > target and left <= right:
    #             cur -= arr[left]
    #             left += 1
            
    #         if cur == target:
    #             res = min(res, prefix[left - 1] + right - left + 1)
    #             prefix[right] = min(prefix[right - 1], right - left + 1)
    #         else:
    #             prefix[right] = prefix[right - 1]

    #     return -1 if res == float('inf') else res

def main():
    sol = Solution()
    print(sol.minSumOfLengths(arr = [3,2,2,4,3], target = 3))
    print(sol.minSumOfLengths(arr = [7,3,4,7], target = 7))
    print(sol.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))

if __name__ == '__main__':
    main()