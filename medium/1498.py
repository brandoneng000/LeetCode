from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        left, right = 0, len(nums) - 1
        res = 0

        nums.sort()
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + 2 ** (right - left)) % mod
                left += 1
            else:
                right -= 1
        
        return res


def main():
    sol = Solution()
    print(sol.numSubseq(nums = [3,5,6,7], target = 9))
    print(sol.numSubseq(nums = [3,3,6,8], target = 10))
    print(sol.numSubseq(nums = [2,3,3,4,6,7], target = 12))

if __name__ == '__main__':
    main()