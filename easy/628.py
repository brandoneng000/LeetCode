from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        INF = 10 ** 33
        max1 = max2 = max3 = -INF
        min1 = min2 = INF

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

    # def maximumProduct(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])
        
    # def maximumProduct(self, nums: List[int]) -> int:
    #     smallest_first = smallest_second = float('inf')
    #     largest_first = largest_second = largest_third = -float('inf')

    #     for num in nums:
    #         if num <= smallest_first:
    #             smallest_second = smallest_first
    #             smallest_first = num
    #         elif num <= smallest_second:
    #             smallest_second = num

    #         if num >= largest_first:
    #             largest_third = largest_second
    #             largest_second = largest_first
    #             largest_first = num
    #         elif num >= largest_second:
    #             largest_third = largest_second
    #             largest_second = num
    #         elif num >= largest_third:
    #             largest_third = num
            
    #     return max(smallest_first * smallest_second * largest_first, largest_first * largest_second * largest_third)

        
def main():
    sol = Solution()
    print(sol.maximumProduct([1,2,3]))
    print(sol.maximumProduct([-1,-2,-3]))
    print(sol.maximumProduct([-1,-2,-3,4]))

if __name__ == '__main__':
    main()
