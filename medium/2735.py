from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [x * k for k in range(n)]

        for i in range(n):
            cur = nums[i]

            for k in range(n):
                cur = min(cur, nums[i - k])
                res[k] += cur
        
        return min(res)


        
def main():
    sol = Solution()
    print(sol.minCost(nums = [20,1,15], x = 5))
    print(sol.minCost(nums = [1,2,3], x = 4))

if __name__ == '__main__':
    main()