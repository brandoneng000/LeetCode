from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0

        for right in range(n):
            if nums[right] - nums[left] > k * 2:
                left += 1
        
        return right - left + 1

        
def main():
    sol = Solution()
    print(sol.maximumBeauty(nums = [4,6,1,2], k = 2))
    print(sol.maximumBeauty(nums = [1,1,1,1], k = 10))

if __name__ == '__main__':
    main()