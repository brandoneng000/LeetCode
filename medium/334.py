from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # first = float('inf')
        # second = float('inf')
        # third = float('inf')

        # for index, n in enumerate(nums):
        #     if n < first and len(nums) - index > 2:
        #         first = n
        #         second = first
        #     elif n > third:
        #         return True
        #     elif n > second and len(nums) - index > 1:
        #         second = n
        #         third = second
        
        #     if n < second and n > first:
        #         second = n
        #         third = second

        # return False
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

def main():
    sol = Solution()
    print(sol.increasingTriplet([1,2,3,4,5]))
    print(sol.increasingTriplet([5,4,3,2,1]))
    print(sol.increasingTriplet([2,1,5,0,4,6]))
    print(sol.increasingTriplet([20,100,10,12,5,13]))
    print(sol.increasingTriplet([1,5,0,4,1,3]))
    print(sol.increasingTriplet([5,1,6]))

if __name__ == '__main__':
    main()