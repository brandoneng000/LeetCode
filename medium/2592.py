from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        left = 0

        for right in range(1, n):
            if nums[left] > nums[right]:
                left += 1
        
        return left
        
def main():
    sol = Solution()
    print(sol.maximizeGreatness([1,3,5,2,1,3,1]))
    print(sol.maximizeGreatness([1,2,3,4]))

if __name__ == '__main__':
    main()