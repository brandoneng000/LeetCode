from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        nums += nums[:ones]
        cur_count = max_count = nums[:ones].count(1)

        for i in range(n):
            cur_count -= nums[i]
            cur_count += nums[i + ones]
            max_count = max(max_count, cur_count)
        
        return ones - max_count
        
        
def main():
    sol = Solution()
    print(sol.minSwaps([0,1,0,1,1,0,0]))
    print(sol.minSwaps([0,1,1,1,0,0,1,1,0]))
    print(sol.minSwaps([1,1,0,0,1]))

if __name__ == '__main__':
    main()