from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        cnt = [0] * (n + 1)
        tot = [0] * (n + 1)
        last, res = {}, 0

        for r, x in enumerate(nums):
            p = last.get(x, -1)
            c = s = 0
            i = n - p - 1

            while i:
                c += cnt[i]
                s += tot[i]
                i -= i & -i

            res += (n - r) * ((r - p) ** 2 - 2 * (s - p * c))
            i = n - p

            while i <= n:
                cnt[i] += 1
                tot[i] += p
                i += i & -i
            last[x] = r

        return res % MOD

def main():
    sol = Solution()
    print(sol.sumCounts([1,2,1]))
    print(sol.sumCounts([2,2]))

if __name__ == '__main__':
    main()