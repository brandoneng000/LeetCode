from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # res = 0

        # for k in range(len(nums) - 1, -1, -1):
        #     for j in range(k - 1, -1, -1):
        #         if nums[k] - nums[j] == diff:
        #             for i in range(j - 1, -1, -1):
        #                 if nums[j] - nums[i] == diff:
        #                     res += 1
        #                 elif nums[j] - nums[i] > diff:
        #                     break
        #         elif nums[k] - nums[j] > diff:
        #             break

        # return res

        res = 0
        nums = set(nums)

        for num in nums:
            if num + diff in nums and num + diff * 2 in nums:
                res += 1
        
        return res

def main():
    sol = Solution()
    print(sol.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
    print(sol.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))

if __name__ == '__main__':
    main()