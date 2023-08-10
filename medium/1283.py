from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = (left + right) // 2
            cur_total = sum(math.ceil(n / middle) for n in nums)

            if cur_total > threshold:
                left = middle + 1
            else:
                right = middle
        
        return left


def main():
    sol = Solution()
    print(sol.smallestDivisor(nums = [19], threshold = 5))
    print(sol.smallestDivisor(nums = [1,2,5,9], threshold = 6))
    print(sol.smallestDivisor(nums = [44,22,33,11,1], threshold = 5))

if __name__ == '__main__':
    main()