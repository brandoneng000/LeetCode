from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for i, num in enumerate(nums):
            if bin(i).count('1') == k:
                res += num
            
        return res
        
def main():
    sol = Solution()
    print(sol.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1))
    print(sol.sumIndicesWithKSetBits(nums = [4,3,2,1], k = 2))

if __name__ == '__main__':
    main()