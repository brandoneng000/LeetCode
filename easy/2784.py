from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(set(nums))
        
        if len(nums) != n + 1:
            return False
        
        for i, num in zip(range(1, n + 1), sorted(set(nums))):
            if i != num:
                return False
        
        if nums.count(n) != 2:
            return False

        return True

        
def main():
    sol = Solution()
    print(sol.isGood([2, 1, 3]))
    print(sol.isGood([1, 3, 3, 2]))
    print(sol.isGood([1, 1]))
    print(sol.isGood([3, 4, 4, 1, 2, 1]))

if __name__ == '__main__':
    main()