from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_len = 1
        nums_set = set(nums)

        for prev, curr in zip(nums, nums[1:]):
            if curr == prev + 1:
                prefix_len += 1
            else:
                break

        res = (nums[prefix_len - 1] + nums[0]) * prefix_len // 2

        while res in nums_set:
            res += 1

        return res

    # def missingInteger(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     prefix = nums[0]

    #     for i in range(1, n):
    #         if nums[i - 1] + 1 == nums[i]:
    #             prefix += nums[i]
    #         else:
    #             break
        
    #     nums.sort()
    #     for i in range(n):
    #         if prefix == nums[i]:
    #             prefix += 1
        
    #     return prefix
        
def main():
    sol = Solution()
    print(sol.missingInteger([1,2,3,2,5]))
    print(sol.missingInteger([3,4,5,1,12,14,13]))

if __name__ == '__main__':
    main()