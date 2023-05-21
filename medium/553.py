from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return f"{nums[0]}"
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            return f"{nums[0]}/({'/'.join(str(n) for n in nums[1:])})"

def main():
    sol = Solution()
    print(sol.optimalDivision([1000,100,10,2]))
    print(sol.optimalDivision([2,3,4]))

if __name__ == '__main__':
    main()