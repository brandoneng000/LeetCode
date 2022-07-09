from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])
        smallest_first = smallest_second = float('inf')
        largest_first = largest_second = largest_third = -float('inf')

        for num in nums:
            if num <= smallest_first:
                smallest_second = smallest_first
                smallest_first = num
            elif num <= smallest_second:
                smallest_second = num

            if num >= largest_first:
                largest_third = largest_second
                largest_second = largest_first
                largest_first = num
            elif num >= largest_second:
                largest_third = largest_second
                largest_second = num
            elif num >= largest_third:
                largest_third = num
            
        return max(smallest_first * smallest_second * largest_first, largest_first * largest_second * largest_third)

        
def main():
    sol = Solution()
    print(sol.maximumProduct([1,2,3]))
    print(sol.maximumProduct([-1,-2,-3]))
    print(sol.maximumProduct([-1,-2,-3,4]))

if __name__ == '__main__':
    main()
