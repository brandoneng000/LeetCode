from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = sum(nums)
        res = []

        for i, num in enumerate(nums):
            right -= num
            res.append((num * i - left) + (right - num * (n - i - 1)))
            left += num

        return res

def main():
    sol = Solution()
    print(sol.getSumAbsoluteDifferences([2,3,5]))
    print(sol.getSumAbsoluteDifferences([1,4,6,8,10]))

if __name__ == '__main__':
    main()