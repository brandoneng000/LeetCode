from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        smallest = min(nums)
        largest = max(nums)

        for n in nums:
            if n != smallest and n != largest:
                return n
        
def main():
    sol = Solution()
    print(sol.findNonMinOrMax([3,2,1,4]))
    print(sol.findNonMinOrMax([1,2]))
    print(sol.findNonMinOrMax([2,1,3]))

if __name__ == '__main__':
    main()