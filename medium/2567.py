from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        INF = 10 ** 33
        mn1 = mn2 = mn3 = INF
        mx1 = mx2 = mx3 = -INF

        for num in nums:
            if num < mn1:
                mn1, mn2, mn3 = num, mn1, mn2
            elif num < mn2:
                mn2, mn3 = num, mn2
            elif num < mn3:
                mn3 = num

            if num > mx1:
                mx1, mx2, mx3 = num, mx1, mx2
            elif num > mx2:
                mx2, mx3 = num, mx2
            elif num > mx3:
                mx3 = num

        return min(mx1 - mn3, mx2 - mn2, mx3 - mn1)


    # def minimizeSum(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
        

def main():
    sol = Solution()
    print(sol.minimizeSum([1,4,7,8,5]))
    print(sol.minimizeSum([1,4,3]))

if __name__ == '__main__':
    main()