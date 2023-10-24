from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0

        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        res = pos

        for i in range(1, n):
            if nums[i] > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0

            res = max(res, pos)
        
        return res
        


    # def getMaxLen(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     last_negative = -1
    #     left = 0

    #     for i in range(n - 1, -1, -1):
    #         if nums[i] < 0:
    #             last_negative = i
    #             break
        
    #     cur = 1
    #     cur_size = 0
    #     res = 0

    #     for right in range(n):
    #         if nums[right] == 0:
    #             while left < right and cur_size > res:
    #                 cur //= nums[left]
    #                 cur_size -= 1
    #                 left += 1

    #                 if cur > 0:
    #                     res = max(res, cur_size)

    #             cur = 1
    #             cur_size = 0
    #             left = right + 1
    #         else:
    #             cur *= nums[right]
    #             cur_size += 1

    #             while right == last_negative and left <= right and cur < 0:
    #                 cur //= nums[left]
    #                 left += 1
    #                 cur_size -= 1
                
    #             if cur > 0:
    #                 res = max(res, cur_size)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.getMaxLen(nums = [25,10,-28,-12,-13,-16,-13,28,5,21,28,4,0,-1]))
    print(sol.getMaxLen(nums = [1,-3,0,0,-5,12]))
    print(sol.getMaxLen(nums = [1,-2,-3,4]))
    print(sol.getMaxLen(nums = [0,1,-2,-3,-4]))
    print(sol.getMaxLen(nums = [-1,-2,-3,0,1]))

if __name__ == '__main__':
    main()