from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1

        for i in range(n):
            cur = nums[i]
            for j in range(i + 1, n):
                if cur & nums[j] != 0:
                    break

                cur |= nums[j]
                res = max(res, j - i + 1)
        
        return res


    # def longestNiceSubarray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     res = 0
    #     cur = 0
    #     left = 0
        
    #     for right in range(n):
    #         while left < right and cur & nums[right]:
    #             cur ^= nums[left]
    #             left += 1
            
    #         res = max(res, right - left + 1)
    #         cur |= nums[right]

    #     return res


        
def main():
    sol = Solution()
    print(sol.longestNiceSubarray([1,3,8,48,10]))
    print(sol.longestNiceSubarray([3,1,5,11,13]))

if __name__ == '__main__':
    main()