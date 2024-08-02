from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if not sum(nums):
            return 0

        mod = 1000000007
        prev = -1
        res = 1

        for i, bit in enumerate(nums):
            if bit == 1 and prev == -1:
                prev = i
            elif bit == 1:
                res = (res * (i - prev)) % mod
                prev = i
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.numberOfGoodSubarraySplits([1,0,0,0,1,0,0,0,1,0,1]))
    print(sol.numberOfGoodSubarraySplits([0,1,0,0,1]))
    print(sol.numberOfGoodSubarraySplits([0,1,0]))

if __name__ == '__main__':
    main()