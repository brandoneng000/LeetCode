from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        reduce = 0
        nums.sort()

        for index, num in enumerate(nums):
            total -= num
            reduce += num
            if total <= reduce:
                return sorted(nums[index:], reverse=True)

        

        
def main():
    sol = Solution()
    print(sol.minSubsequence([4,3,10,9,8]))
    print(sol.minSubsequence([4,4,7,6,7]))

if __name__ == '__main__':
    main()