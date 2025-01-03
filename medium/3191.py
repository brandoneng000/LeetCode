from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n - 2):
            if not nums[i]:
                res += 1
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
        
        if nums[-1] == nums[-2] == nums[-3] == 1:
            return res
        
        return -1
        
def main():
    sol = Solution()
    print(sol.minOperations([0,1,1,1,0,0]))
    print(sol.minOperations([0,1,1,1]))

if __name__ == '__main__':
    main()