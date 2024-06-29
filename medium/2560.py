from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)

        while left < right:
            middle = (left + right) // 2

            last = take = 0

            for num in nums:
                if last:
                    last = 0
                    continue

                if num <= middle:
                    take += 1
                    last = 1
            
            if take >= k:
                right = middle
            else:
                left = middle + 1
        
        return left
        
def main():
    sol = Solution()
    print(sol.minCapability(nums = [2,3,5,9], k = 2))
    print(sol.minCapability(nums = [2,7,9,3,1], k = 2))

if __name__ == '__main__':
    main()