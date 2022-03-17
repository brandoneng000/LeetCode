from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difference = 10000000
        nums.sort()
        for index, num in enumerate(nums):
            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = nums[left] + nums[right] + num
                sum = target - three_sum
                if sum == 0:
                    return target
                if abs(sum) < abs(target - difference):
                    difference = three_sum
                if sum < 0:
                    right -= 1
                else:
                    left += 1
        
        return difference
                

        
def main():
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))
    print(sol.threeSumClosest([1,1,-1,-1,3], -1))

if __name__ == '__main__':
    main()