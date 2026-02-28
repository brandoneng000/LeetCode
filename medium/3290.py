from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp0 = dp1 = dp2 = dp3 = -10 ** 33
        a0, a1, a2, a3 = a

        for num in b:
            dp3 = max(dp3, dp2 + a3 * num)
            dp2 = max(dp2, dp1 + a2 * num)
            dp1 = max(dp1, dp0 + a1 * num)
            dp0 = max(dp0, a0 * num)
        
        return dp3


    # def maxScore(self, a: List[int], b: List[int]) -> int:
    #     n = len(b)
    #     res = -10 * 33

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             for u in range(j + 1, n):
    #                 for v in range(u + 1, n):
    #                     res = max(res, a[0] * b[i] + a[1] * b[j] + a[2] * b[u] + a[3] * b[v])
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]))
    print(sol.maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]))

if __name__ == '__main__':
    main()