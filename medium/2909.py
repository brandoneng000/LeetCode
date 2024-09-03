from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = nums[:]
        prefix = nums[0]
        res = float('inf')

        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])
        
        for i in range(1, n - 1):
            if prefix < nums[i] > suffix[i + 1]:
                res = min(res, prefix + nums[i] + suffix[i + 1])
            prefix = min(prefix, nums[i])
        
        return res if res != float('inf') else -1


def main():
    sol = Solution()
    print(sol.minimumSum([8,6,1,5,3]))
    print(sol.minimumSum([5,4,8,7,10,2]))
    print(sol.minimumSum([6,5,4,3,4,5]))

if __name__ == '__main__':
    main()