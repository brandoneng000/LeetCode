from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = nums.copy()

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        res, first_max, second_max = prefix[firstLen + secondLen - 1], prefix[firstLen - 1], prefix[secondLen - 1]

        for i in range(firstLen + secondLen, len(prefix)):
            first_max = max(first_max, prefix[i - secondLen] - prefix[i - firstLen - secondLen])
            res = max(res, first_max + prefix[i] - prefix[i - secondLen])
        
        for i in range(firstLen + secondLen, len(prefix)):
            second_max = max(second_max, prefix[i - firstLen] - prefix[i - firstLen - secondLen])
            res = max(res, second_max + prefix[i] - prefix[i - firstLen])
        
        return res

    # def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    #     def max_sum(first: int, second: int):
    #         large = res = 0

    #         for i in range(first + second, len(prefix)):
    #             large = max(large, prefix[i - second] - prefix[i - first - second])
    #             res = max(res, large + prefix[i] - prefix[i - second])
            
    #         return res
        
    #     prefix = [0] * (len(nums) + 1)
    #     for i, val in enumerate(nums):
    #         prefix[i + 1] = prefix[i] + val

    #     return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))
    


def main():
    sol = Solution()
    print(sol.maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2))
    print(sol.maxSumTwoNoOverlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2))
    print(sol.maxSumTwoNoOverlap(nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3))

if __name__ == '__main__':
    main()