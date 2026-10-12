from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        cnt = [0] * 30
        res = 0

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1

        for _ in range(k):
            cur = 0

            for j in range(29, -1, -1):
                if cnt[j] > 0:
                    cur |= 1 << j
                    cnt[j] -= 1

            res = (res + cur * cur) % MOD

        return res

def main():
    sol = Solution()
    print(sol.maxSum(nums = [2,6,5,8], k = 2))
    print(sol.maxSum(nums = [4,5,4,7], k = 3))

if __name__ == '__main__':
    main()