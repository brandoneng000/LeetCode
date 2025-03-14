from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0

        for num in nums:
            count += num % 2 == 0

            if count > 1:
                return True
        
        return False
        
def main():
    sol = Solution()
    print(sol.hasTrailingZeros([1,2,3,4,5]))
    print(sol.hasTrailingZeros([2,4,8,16]))
    print(sol.hasTrailingZeros([1,3,5,7,9]))

if __name__ == '__main__':
    main()