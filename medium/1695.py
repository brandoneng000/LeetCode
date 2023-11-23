from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        used = set()
        cur = 0
        res = 0

        for right in range(n):
            while nums[right] in used:
                cur -= nums[left]
                used.remove(nums[left])
                left += 1
            
            used.add(nums[right])
            cur += nums[right]
            res = max(res, cur)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumUniqueSubarray([4,2,4,5,6]))
    print(sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))

if __name__ == '__main__':
    main()