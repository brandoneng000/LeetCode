from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_num = 2 ** maximumBit - 1
        res = []
        cur = 0

        for num in nums:
            cur ^= num
        
        for i in range(n - 1, -1, -1):
            res.append(cur ^ max_num)
            cur ^= nums[i]
        
        return res

        
def main():
    sol = Solution()
    print(sol.getMaximumXor(nums = [0,1,1,3], maximumBit = 2))
    print(sol.getMaximumXor(nums = [2,3,4,7], maximumBit = 3))
    print(sol.getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3))

if __name__ == '__main__':
    main()