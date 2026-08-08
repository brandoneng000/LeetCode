from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        INF = 10 ** 33
        res = INF

        for size in range(l, r + 1):
            for i in range(n - size + 1):
                cur = sum(nums[i: i + size])

                if cur > 0:
                    res = min(res, cur)

        return res if res != INF else -1

def main():
    sol = Solution()
    print(sol.minimumSumSubarray(nums = [7, 3], l = 2, r = 2))
    print(sol.minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3))
    print(sol.minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3))
    print(sol.minimumSumSubarray(nums = [1, 2, 3, 4], l = 2, r = 4))

if __name__ == '__main__':
    main()