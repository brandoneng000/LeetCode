from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(1, n - 1):
            if (nums[i - 1] + nums[i + 1]) * 2 == nums[i]:
                res += 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.countSubarrays([1,2,1,4,1]))
    print(sol.countSubarrays([1,1,1]))

if __name__ == '__main__':
    main()