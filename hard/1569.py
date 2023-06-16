from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1000000007
        pascals = [[0 for i in range(j + 1)] for j in range(len(nums))]

        for row in pascals:
            row[0] = 1
            row[-1] = 1
        
        for i in range(2, len(pascals)):
            for j in range(1, len(pascals[i]) - 1):
                pascals[i][j] = pascals[i - 1][j - 1] + pascals[i - 1][j]

        def dfs(nums: List[int]):
            if len(nums) < 3:
                return 1
            
            root = nums[0]

            left = [num for num in nums if num < root]
            right = [num for num in nums if num > root]
            return (pascals[len(nums) - 1][len(left)] * (dfs(left) * dfs(right) % mod)) % mod

        return dfs(nums) - 1


def main():
    sol = Solution()
    print(sol.numOfWays([2,1,3]))
    print(sol.numOfWays([3,4,5,1,2]))
    print(sol.numOfWays([1,2,3]))

if __name__ == '__main__':
    main()