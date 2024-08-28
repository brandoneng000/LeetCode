from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        q, r = divmod(target, total)
        nums += nums
        n = len(nums)
        left = 0
        res = float('inf')
        cur = 0

        if r == 0:
            return n // 2 * q

        for right in range(n):
            cur += nums[right]

            while left < right and cur > r:
                cur -= nums[left]
                left += 1
            
            if cur == r:
                res = min(res, right - left + 1)
        
        return n // 2 * q + res if res != float('inf') else -1

        
def main():
    sol = Solution()
    print(sol.minSizeSubarray(nums = [1,2,3], target = 6))
    print(sol.minSizeSubarray(nums = [1,2,3], target = 5))
    print(sol.minSizeSubarray(nums = [1,1,1,2,3], target = 4))
    print(sol.minSizeSubarray(nums = [2,4,6,8], target = 3))

if __name__ == '__main__':
    main()