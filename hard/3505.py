from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        def prune(h: List[int], sign: int) -> None:
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance() -> None:
            nonlocal left_size, right_size, sum_left, sum_right

            if left_size > right_size + 1:
                num = -heappop(left)
                heappush(right, num)
                sum_right += num
                sum_left -= num
                right_size += 1
                left_size -= 1
                prune(left, -1)
            elif right_size > left_size:
                num = heappop(right)
                heappush(left, -num)
                sum_left += num
                sum_right -= num
                left_size += 1
                right_size -= 1
                prune(right, 1)
        
        n = len(nums)
        INF = 10 ** 33
        left, right = [], []
        delayed = defaultdict(int)
        left_size = right_size = 0
        sum_left = sum_right = 0
        ops = [0] * n

        for i, num in enumerate(nums):
            if not left or num <= -left[0]:
                heappush(left, -num)
                left_size += 1
                sum_left += num
            else:
                heappush(right, num)
                right_size += 1
                sum_right += num

            balance()

            if i >= x:
                num = nums[i - x]
                delayed[num] += 1

                if num <= -left[0]:
                    left_size -= 1
                    sum_left -= num

                    if num == -left[0]:
                        prune(left, -1)
                else:
                    right_size -= 1
                    sum_right -= num

                    if num == right[0]:
                        prune(right, 1)
                balance()

            if i >= x - 1:
                mid = -left[0]
                ops[i] = sum_right - sum_left + mid * (left_size - right_size)

        dp = [[0] + [INF] * k for _ in range(n)]

        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = ops[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1]

        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j])

        return dp[n - 1][k]


def main():
    sol = Solution()
    print(sol.minOperations(nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2))
    print(sol.minOperations(nums = [9,-2,-2,-2,1,5], x = 2, k = 2))

if __name__ == '__main__':
    main()