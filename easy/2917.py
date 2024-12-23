from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        res = 0

        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
        
        for i in range(32):
            if bits[i] >= k:
                res |= 1 << i
        
        return res

        
def main():
    sol = Solution()
    print(sol.findKOr(nums = [7,12,9,8,9,15], k = 4))
    print(sol.findKOr(nums = [2,12,1,11,4,5], k = 6))
    print(sol.findKOr(nums = [10,8,5,9,11,6,8], k = 1))

if __name__ == '__main__':
    main()