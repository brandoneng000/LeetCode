from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 1

        while res in nums_set:
            res <<= 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.minImpossibleOR([2,1]))
    print(sol.minImpossibleOR([5,3,2]))

if __name__ == '__main__':
    main()