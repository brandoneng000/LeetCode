from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 10 ** 18
        left = 0

        for right in range(n):
            if nums[right] <= nums[left] * k:
                res = min(res, left + (n - right) - 1)
            else:
                while nums[right] > nums[left] * k:
                    left += 1
                res = min(res, left + (n - right) - 1)
        
        return res




def main():
    sol = Solution()
    print(sol.minRemoval(nums = [2,1,5], k = 2))
    print(sol.minRemoval(nums = [1,6,2,9], k = 3))
    print(sol.minRemoval(nums = [4,6], k = 2))

if __name__ == '__main__':
    main()