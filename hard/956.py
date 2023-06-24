from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = { 0:0 }

        for r in rods:
            new_dp = dp.copy()

            for diff, taller in dp.items():
                shorter = taller - diff
                
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)

                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)

            dp = new_dp

        return dp.get(0, 0) 

    # def tallestBillboard(self, rods: List[int]) -> int:
    #     def helper(rods: List[int]):
    #         states = set()
    #         states.add((0, 0))
    #         for rod in rods:
    #             new_state = set()
    #             for l, r in states:
    #                 new_state.add((l + rod, r))
    #                 new_state.add((l, r + rod))
    #             states |= new_state
            
    #         dp = {}
    #         for l, r in states:
    #             dp[l - r] = max(dp.get(l - r, 0), l)
    #         return dp
        
    #     first_half = helper(rods[:len(rods) // 2])
    #     second_half = helper(rods[len(rods) // 2:])

    #     res = 0
    #     for diff in first_half:
    #         if -diff in second_half:
    #             res = max(res, first_half[diff] + second_half[-diff])
        
    #     return res


def main():
    sol = Solution()
    print(sol.tallestBillboard([1,2,3,6]))
    print(sol.tallestBillboard([1,2,3,4,5,6]))
    print(sol.tallestBillboard([1,2]))

if __name__ == '__main__':
    main()