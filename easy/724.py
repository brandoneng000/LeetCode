from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_total, right_total = 0, sum(nums)

        for index, num in enumerate(nums):
            right_total -= num
            if left_total == right_total:
                return index
            left_total += num
        
        return -1

def main():
    sol = Solution()
    print(sol.pivotIndex([1,7,3,6,5,6]))
    print(sol.pivotIndex([1,2,3]))
    print(sol.pivotIndex([2,1,-1]))

if __name__ == '__main__':
    main()