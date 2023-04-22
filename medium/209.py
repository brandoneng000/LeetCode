from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')

        for i, n in enumerate(nums):
            total += n
            while total >= target:
                res = min(res, i + 1 - left)
                total -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0



def main():
    sol = Solution()
    print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
    print(sol.minSubArrayLen(target = 4, nums = [1,4,4]))
    print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))

if __name__ == '__main__':
    main()