from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = max(nums)
        dp = [[0] * (n + 1)]
        res = []

        for num in nums:
            temp = dp[-1][:]
            temp[num] += 1
            dp.append(temp)

        for l, r in queries:
            diff = []

            for x, y, i in zip(dp[r + 1], dp[l], range(n + 1)):
                if x != y:
                    diff.append(i)
            res.append(min([b - a for a, b in zip(diff, diff[1:])] or [-1]))
        
        return res

    # def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    #     res = []

    #     for l, r in queries:
    #         cur = nums[l: r + 1]
    #         min_val = float('inf')

    #         for i, a in enumerate(cur):
    #             for b in sorted(set(cur[i + 1:])):
    #                 if a != b:
    #                     min_val = min(min_val, abs(a - b))
            
    #         res.append(min_val if min_val != float('inf') else -1)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.minDifference(nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]))
    print(sol.minDifference(nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]))

if __name__ == '__main__':
    main()