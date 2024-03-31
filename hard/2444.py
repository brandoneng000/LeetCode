from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res = 0
        prev_min_index = prev_max_index = bad_index = -1

        for i in range(n):
            if not minK <= nums[i] <= maxK:
                bad_index = i
            if nums[i] == minK:
                prev_min_index = i
            if nums[i] == maxK:
                prev_max_index = i
            
            res += max(0, min(prev_max_index, prev_min_index) - bad_index)
        
        return res

        
def main():
    sol = Solution()
    print(sol.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(sol.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))

if __name__ == '__main__':
    main()