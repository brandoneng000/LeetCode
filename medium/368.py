from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        div_count = [1] * len(nums)
        prev = [-1] * len(nums)
        max_index = 0
        res = []

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if div_count[i] < div_count[j] + 1:
                        div_count[i] = div_count[j] + 1
                        prev[i] = j
                if div_count[max_index] < div_count[i]:
                    max_index = i
        
        while max_index >= 0:
            res.append(nums[max_index])
            max_index = prev[max_index]
        
        return res

        # if len(nums) <= 1:
        #     return nums
        # nums.sort()
        # dp = [(0, 0)] * len(nums)
        # dp[0] = (1, 0)
        # max_index, max_val = 0, (0, 1)
        # for i in range(1, len(nums)):
        #     dp[i] = max((dp[j][0] + 1, j) for j in range(i + 1) if nums[i] % nums[j] == 0)
        #     if dp[i] > max_val:
        #         max_index, max_val = i, dp[i]

        # i, res = max_index, [nums[max_index]]
        # while i != dp[i][1]:
        #     i = dp[i][1]
        #     res.append(nums[i])
        # return res

        # self.res = []
        # self.cache = {}

        # def helper(cur: List[int], index: int):
        #     if len(cur) > len(self.res):
        #         self.res = cur.copy()
            
        #     for i in range(index, len(nums)):
        #         condition = 0
        #         for val in cur:
        #             if (nums[i], val) not in self.cache:
        #                 self.cache[(nums[i], val)] = (nums[i] % val == 0) or (val % nums[i] == 0)
        #                 self.cache[(val, nums[i])] = self.cache[(nums[i], val)]
        #             condition += self.cache[(nums[i], val)]

        #         if condition == len(cur):
        #             cur.append(nums[i])
        #             helper(cur, i + 1)
        #             cur.pop()

        # helper([], 0)
        # return self.res

def main():
    sol = Solution()
    print(sol.largestDivisibleSubset([1,2,3]))
    print(sol.largestDivisibleSubset([1,2,4,8]))
    print(sol.largestDivisibleSubset([1,2,3,9,12,18]))

if __name__ == '__main__':
    main()