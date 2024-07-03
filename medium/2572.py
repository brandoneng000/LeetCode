from typing import List
from collections import Counter
from math import gcd

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        def count(arr):
            if not arr:
                return 1
            arr1 = []

            for num in arr[1:]:
                if gcd(num, arr[0]) == 1:
                    arr1.append(num)
            
            return (count(arr[1:]) + cnt[arr[0]] * count(arr1)) % mod

        mod = 1000000007
        candidates = set([2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
        cnt = Counter()

        for num in nums:
            if num in candidates:
                cnt[num] += 1

        ones = nums.count(1)
        temp = 1

        for _ in range(ones):
            temp = (temp * 2) % mod

        return (count(list(cnt)) * temp - 1) % mod


def main():
    sol = Solution()
    print(sol.squareFreeSubsets([3,4,4,5]))
    print(sol.squareFreeSubsets([1]))

if __name__ == '__main__':
    main()