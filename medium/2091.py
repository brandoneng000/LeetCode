from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        min_dist_start = min_index + 1
        min_dist_end = n - min_index
        max_dist_start = max_index + 1
        max_dist_end = n - max_index

        res = min(
            max(min_dist_start, max_dist_start),
            min(min_dist_start + max_dist_end, min_dist_end + max_dist_start),
            max(min_dist_end, max_dist_end)
        )

        return res

    # def minimumDeletions(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     INF = 10 ** 33

    #     if n == 1:
    #         return 1
        
    #     max_index = min_index = -1
    #     max_val = -INF
    #     min_val = INF

    #     for i in range(n):
    #         if nums[i] > max_val:
    #             max_val = nums[i]
    #             max_index = i
    #         if nums[i] < min_val:
    #             min_val = nums[i]
    #             min_index = i

    #     left = max(max_index, min_index) + 1
    #     right = n - min(max_index, min_index)
    #     sides = min(max_index, min_index) + (n - max(max_index, min_index)) + 1

    #     return min(left, right, sides)
        
def main():
    sol = Solution()
    print(sol.minimumDeletions([5, -3, -2, 8, 1, 19, -4, 0]))
    print(sol.minimumDeletions([2,10,7,5,4,1,8,6]))
    print(sol.minimumDeletions([0,-4,19,1,8,-2,-3,5]))
    print(sol.minimumDeletions([101]))

if __name__ == '__main__':
    main()