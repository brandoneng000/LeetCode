from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums[0]
        if nums[1] < nums[2]:
            min_one = nums[1]
            min_two = nums[2]
        else:
            min_two = nums[1]
            min_one = nums[2]

        for i in range(3, n):
            if nums[i] < min_one:
                min_one, min_two = nums[i], min_one
            elif nums[i] < min_two:
                min_two = nums[i]
        
        return start + min_one + min_two

    # def minimumCost(self, nums: List[int]) -> int:
    #     return nums[0] + sum(sorted(nums[1:])[:2])
        
def main():
    sol = Solution()
    print(sol.minimumCost([1,2,3,12]))
    print(sol.minimumCost([5,4,3]))
    print(sol.minimumCost([10,3,1,1]))

if __name__ == '__main__':
    main()