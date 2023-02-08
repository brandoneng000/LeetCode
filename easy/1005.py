from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k > 0:
            negative = min(nums)

            if negative == 0:
                break
            else:
                nums[nums.index(negative)] = -negative
            k -= 1

        return sum(nums)


def main():
    sol = Solution()
    print(sol.largestSumAfterKNegations(nums = [4,2,3], k = 1))
    print(sol.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
    print(sol.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))

if __name__ == '__main__':
    main()