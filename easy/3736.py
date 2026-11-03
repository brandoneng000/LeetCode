from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        res = 0

        for num in nums:
            res += max_num - num

        return res


def main():
    sol = Solution()
    print(sol.minMoves([2,1,3]))
    print(sol.minMoves([4,4,5]))

if __name__ == '__main__':
    main()