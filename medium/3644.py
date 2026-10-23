from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = 4294967295

        for i in range(n):
            if nums[i] != i:
                res &= nums[i]

        return res if res != 4294967295 else 0


def main():
    sol = Solution()
    print(sol.sortPermutation([0,3,2,1]))
    print(sol.sortPermutation([0,1,3,2]))
    print(sol.sortPermutation([3,2,1,0]))

if __name__ == '__main__':
    main()