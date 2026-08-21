from typing import List
from math import lcm
from bisect import bisect_left

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(mid):
            tot = 0

            for i in range(1, n + 1):
                q = (1 << i) - 1
                lim = 1 << n
                sgn = ((i & 1) << 1) - 1

                while q < lim:
                    x = 1 

                    for j in range(n):
                        if (q >> j) & 1:
                            x = lcm(x, A[j])

                    tot += (mid // x) * sgn

                    c = q & -q
                    r = q + c
                    q = (((r ^ q) >> 2) // c) | r

            return tot >= k

        coins.sort()
        A = []

        for c in coins:
            if all(c % x for x in A):
                A.append(c)

        n = len(A)
        return bisect_left(range(A[0] * k + 1), True, lo=k, key=check)

    # def findKthSmallest(self, coins: List[int], k: int) -> int:
    #     n = len(coins)
    #     cur = coins[::]
    #     res = 10 ** 33

    #     for _ in range(k):
    #         res = min(cur)

    #         for i in range(n):
    #             if cur[i] == res:
    #                 cur[i] += coins[i]

    #     return res

    # def findKthSmallest(self, coins: List[int], k: int) -> int:
    #     res = set()

    #     for c in coins:
    #         for i in range(1, k + 1):
    #             res.add(c * i)

    #     return sorted(res)[k - 1]

def main():
    sol = Solution()
    print(sol.findKthSmallest(coins = [3,6,9], k = 3))
    print(sol.findKthSmallest(coins = [5,2], k = 7))

if __name__ == '__main__':
    main()