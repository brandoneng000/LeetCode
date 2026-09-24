from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(num: int):
            res = 0

            while num:
                num, r = divmod(num, 10)
                res += r

            return res

        n = len(nums)

        for i in range(n):
            if i == digit_sum(nums[i]):
                return i

        return -1

def main():
    sol = Solution()
    print(sol.smallestIndex([1,3,2]))
    print(sol.smallestIndex([1,10,11]))
    print(sol.smallestIndex([1,2,3]))

if __name__ == '__main__':
    main()