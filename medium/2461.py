from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur = 0
        res = 0
        cur_set = set()
        left = 0

        for right in range(n):
            while (cur_set and nums[right] in cur_set) or len(cur_set) == k:
                cur_set.remove(nums[left])
                cur -= nums[left]
                left += 1
            
            cur_set.add(nums[right])
            cur += nums[right]

            if len(cur_set) == k:
                res = max(res, cur)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))
    print(sol.maximumSubarraySum(nums = [4,4,4], k = 3))

if __name__ == '__main__':
    main()