from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        res = 1

        while res <= n:
            res <<= 1

        return res



def main():
    sol = Solution()
    print(sol.uniqueXorTriplets([1,2]))
    print(sol.uniqueXorTriplets([3,1,2]))

if __name__ == '__main__':
    main()