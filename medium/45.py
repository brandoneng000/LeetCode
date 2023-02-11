from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = len(nums) - 1
        current_end = 0
        current_far = 0

        for index in range(end):
            current_far = max(current_far, index + nums[index])
            if index == current_end:
                jumps += 1
                current_end = current_far

                if current_end >= end:
                    break
        
        return jumps

def main():
    sol = Solution()
    print(sol.jump([2,3,1,1,4]))
    print(sol.jump([2,3,0,1,4]))
    print(sol.jump([2]))
    print(sol.jump([3,3,3,3,3,3,3,3]))
    print(sol.jump([1,2,3]))
    print(sol.jump([1,2]))
    print(sol.jump([3,2,1]))
    print(sol.jump([10,9,8,7,6,5,4,3,2,1,1,0]))

if __name__ == '__main__':
    main()