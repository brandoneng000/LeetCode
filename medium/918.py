from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_max = 0
        min_sum = float('inf')
        cur_min = 0
        total = 0

        for n in nums:
            cur_max = max(cur_max, 0) + n
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min, 0) + n
            min_sum = min(min_sum, cur_min)
            total += n

        return max_sum if total == min_sum else max(max_sum, total - min_sum)
    
def main():
    sol = Solution()
    print(sol.maxSubarraySumCircular([1,-2,3,-2]))
    print(sol.maxSubarraySumCircular([5,-3,5]))
    print(sol.maxSubarraySumCircular([-3,-2,-3]))

if __name__ == '__main__':
    main()