from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        max_ele = max(nums)
        left = 0
        res = 0

        for right in range(n):
            if max_ele == nums[right]:
                count += 1
            while count == k:
                if nums[left] == max_ele:
                    count -= 1
                left += 1
            
            res += left

        return res
        
def main():
    sol = Solution()
    print(sol.countSubarrays(nums = [1,3,2,3,3], k = 2))
    print(sol.countSubarrays(nums = [1,4,2,1], k = 3))

if __name__ == '__main__':
    main()