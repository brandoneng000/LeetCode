import collections

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def calc_power(x: int):
            if x in dp:
                return dp[x]
            
            dp[x] = 1 + calc_power( 3 * x + 1 if x % 2 else x // 2)
            return dp[x]

        dp = { 1: 0 }
        nums = [ (calc_power(x), x) for x in range(lo, hi + 1) ]

        return sorted(nums)[k - 1][1]

    # def getKth(self, lo: int, hi: int, k: int) -> int:
    #     def calc_power(x: int) -> int:
    #         step = 0

    #         while x != 1:
    #             step += 1
    #             if x % 2:
    #                 x = 3 * x + 1
    #             else:
    #                 x = x // 2
            
    #         return step

    #     nums = sorted(list(range(lo, hi + 1)), key=calc_power)
    #     return nums[k - 1]


def main():
    sol = Solution()
    print(sol.getKth(lo = 12, hi = 15, k = 2))
    print(sol.getKth(lo = 7, hi = 11, k = 4))

if __name__ == '__main__':
    main()