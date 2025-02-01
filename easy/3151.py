from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False

        return True
        

def main():
    sol = Solution()
    print(sol.isArraySpecial([1]))
    print(sol.isArraySpecial([2,1,4]))
    print(sol.isArraySpecial([4,3,1,6]))

if __name__ == '__main__':
    main()