from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # from collections import Counter
        # size = len(nums)
        # n = size // 2
        # nums_count = Counter(nums)

        # for num in nums_count:
        #     if nums_count[num] == n:
        #         return num
        return (sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1)


def main():
    sol = Solution()
    print(sol.repeatedNTimes([1,2,3,3]))
    print(sol.repeatedNTimes([2,1,2,5,3,2]))
    print(sol.repeatedNTimes([5,1,5,2,5,3,5,4]))

if __name__ == '__main__':
    main()