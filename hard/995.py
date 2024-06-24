from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        flipped = [False] * n
        prev_flips = 0

        for i in range(n):
            if i >= k:
                if flipped[i - k]:
                    prev_flips -= 1
            
            if prev_flips % 2 == nums[i]:
                if i + k > n:
                    return -1
                
                prev_flips += 1
                flipped[i] = True
                res += 1
        
        return res

    # def minKBitFlips(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     res = 0

    #     for i in range(n):
    #         if nums[i] == 0:
    #             if i + k <= n:
    #                 for j in range(i, i + k):
    #                     nums[j] ^= 1
    #                 res += 1
    #             else:
    #                 return -1
        
    #     return res

        
def main():
    sol = Solution()
    # print(sol.minKBitFlips(nums = [0,1,0], k = 1))
    # print(sol.minKBitFlips(nums = [1,1,0], k = 2))
    print(sol.minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3))

if __name__ == '__main__':
    main()