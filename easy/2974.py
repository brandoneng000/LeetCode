from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        for i in range(0, n, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        return nums

        
def main():
    sol = Solution()
    print(sol.numberGame([5,4,2,3]))
    print(sol.numberGame([2,5]))

if __name__ == '__main__':
    main()