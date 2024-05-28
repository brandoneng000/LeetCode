from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest = max(nums)
        res = cur = 0

        for num in nums:
            if num == largest:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        
        return res
        
def main():
    sol = Solution()
    print(sol.longestSubarray([1,2,3,3,2,2]))
    print(sol.longestSubarray([1,2,3,4]))

if __name__ == '__main__':
    main()