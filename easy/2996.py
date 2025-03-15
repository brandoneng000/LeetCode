from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = nums[0]

        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                prefix += nums[i]
            else:
                break
        
        nums.sort()
        for i in range(n):
            if prefix == nums[i]:
                prefix += 1
        
        return prefix
        
def main():
    sol = Solution()
    print(sol.missingInteger([1,2,3,2,5]))
    print(sol.missingInteger([3,4,5,1,12,14,13]))

if __name__ == '__main__':
    main()