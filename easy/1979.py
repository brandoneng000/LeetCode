from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        while small:
            small, large = large % small, small
        
        return large

    # def findGCD(self, nums: List[int]) -> int:
    #     small = min(nums)
    #     large = max(nums)

    #     for i in range(small, 0, -1):
    #         if small % i == 0 and large % i == 0:
    #             return i

def main():
    sol = Solution()
    print(sol.findGCD([2,5,6,9,10]))
    print(sol.findGCD([7,5,6,8,3]))
    print(sol.findGCD([3,3]))

if __name__ == '__main__':
    main()