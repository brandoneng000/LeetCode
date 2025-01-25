from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    res = max(res, x ^ y)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumStrongPairXor([1,2,3,4,5]))
    print(sol.maximumStrongPairXor([10,100]))
    print(sol.maximumStrongPairXor([5,6,25,30]))

if __name__ == '__main__':
    main()