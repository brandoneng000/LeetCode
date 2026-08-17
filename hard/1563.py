from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]
        left_ptr = [0] * n
        right_ptr = list(range(n))

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

            left_ptr[i] = i - 1
            right_ptr[i] = i

        for size in range(2, n + 1):
            for left in range(n - size + 1):
                right = left + size - 1
                total = prefix[right + 1] - prefix[left]

                while left_ptr[left] + 1 <= right - 1:
                    k = left_ptr[left] + 1
                    left_sum = prefix[k + 1] - prefix[left]

                    if 2 * left_sum > total:
                        break

                    left_ptr[left] += 1

                while right_ptr[left] <= right - 1:
                    k = right_ptr[left]
                    left_sum = prefix[k + 1] - prefix[left]

                    if 2 * left_sum >= total:
                        break

                    right_ptr[left] += 1

                best = 0

                if left_ptr[left] >= left:
                    best = left_best[left][left_ptr[left]]

                if right_ptr[left] <= right - 1:
                    best = max(best, right_best[right_ptr[left] + 1][right])

                dp[left][right] = best

                left_best[left][right] = max(
                    left_best[left][right - 1], 
                    dp[left][right] + total
                )

                right_best[left][right] = max(
                    right_best[left + 1][right],
                    dp[left][right] + total
                )
                
        return dp[0][n - 1]


def main():
    sol = Solution()
    print(sol.stoneGameV([6,2,3,4,5,5]))
    print(sol.stoneGameV([7,7,7,7,7,7,7]))
    print(sol.stoneGameV([4]))

if __name__ == '__main__':
    main()