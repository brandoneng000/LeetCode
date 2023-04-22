from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        
        return -1

def main():
    sol = Solution()
    print(sol.findMiddleIndex([2,3,-1,8,4]))
    print(sol.findMiddleIndex([1,-1,4]))
    print(sol.findMiddleIndex([2,5]))

if __name__ == '__main__':
    main()