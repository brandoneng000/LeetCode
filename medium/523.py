from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = { 0: 0 }
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in cache:
                cache[s % k] = i + 1
            elif cache[s % k] < i:
                return True
        return False

        # def brute_force(cur: List[int], index: int):
        #     if len(cur) >= 2 and sum(cur) % k == 0:
        #         return True
        #     if index == len(nums):
        #         return False

        #     return brute_force([], index + 1) or brute_force(cur + [nums[index]], index + 1)
        
        # return brute_force([], 0)


def main():
    sol = Solution()
    # print(sol.checkSubarraySum(nums = [0], k = 2))
    # print(sol.checkSubarraySum(nums = [1, 0], k = 2))
    print(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6))
    print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 6))
    print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13))

if __name__ == '__main__':
    main()