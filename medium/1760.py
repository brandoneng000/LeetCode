from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = (left + right) // 2
            if sum((ball - 1) // middle for ball in nums) > maxOperations:
                left = middle + 1
            else:
                right = middle
            
        return left
        
def main():
    sol = Solution()
    print(sol.minimumSize(nums = [9], maxOperations = 2))
    print(sol.minimumSize(nums = [2,4,8,2], maxOperations = 4))

if __name__ == '__main__':
    main()