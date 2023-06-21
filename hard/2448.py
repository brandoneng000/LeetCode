from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = sorted([n, c] for n, c in zip(nums, cost))

        prefix = [0] * len(nums)
        prefix[0] = nums_cost[0][1]
        for i in range(1, len(nums)):
            prefix[i] = nums_cost[i][1] + prefix[i - 1]

        total = 0
        for i in range(1, len(nums)):
            total += nums_cost[i][1] * (nums_cost[i][0] - nums_cost[0][0])
        
        print(prefix)
        print(total)
        res = total

        for i in range(1, len(nums)):
            gap = nums_cost[i][0] - nums_cost[i - 1][0]
            total += prefix[i - 1] * gap
            total -= gap * (prefix[len(nums) - 1] - prefix[i - 1])
            res = min(res, total)

        return res

        # prefix = [0] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] != nums[j]:
        #             prefix[j] += abs(nums[i] - nums[j]) * cost[i]
        
        # return min(prefix)


def main():
    sol = Solution()
    print(sol.minCost(nums = [1,3,5,2], cost = [2,3,1,14]))
    print(sol.minCost(nums = [2,2,2,2,2], cost = [4,2,8,1,3]))

if __name__ == '__main__':
    main()