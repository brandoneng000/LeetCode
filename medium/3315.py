from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            cur = -1
            d = 1

            while (num & d) != 0:
                cur = num - d
                d <<= 1
            res.append(cur)

        return res 


def main():
    sol = Solution()
    print(sol.minBitwiseArray([2,3,5,7]))
    print(sol.minBitwiseArray([11,13,31]))

if __name__ == '__main__':
    main()