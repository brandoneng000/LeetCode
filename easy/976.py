from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest_side = max(nums)
        nums.remove(largest_side)
        second = max(nums)
        nums.remove(second)
        third = max(nums)
        nums.remove(third)

        while largest_side + second <= third or second + third <= largest_side or largest_side + third <= second:
            if not nums:
                return 0
            largest_side = second
            second = third
            third = max(nums)
            nums.remove(third)
        
        return largest_side + second + third



def main():
    sol = Solution()
    print(sol.largestPerimeter([2,1,2]))
    print(sol.largestPerimeter([1,2,1,10]))

if __name__ == '__main__':
    main()