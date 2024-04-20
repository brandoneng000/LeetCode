from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, sum(nums)
        min_min = float('inf')
        res = -1

        for i in range(n):
            left += nums[i]
            right -= nums[i]
            cur_min = abs(left // (i + 1) - right // max(n - i - 1, 1))
            
            if min_min > cur_min:
                min_min = cur_min
                res = i
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumAverageDifference([2,5,3,9,5,3]))
    print(sol.minimumAverageDifference([0]))

if __name__ == '__main__':
    main()