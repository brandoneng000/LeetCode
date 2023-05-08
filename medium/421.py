from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0

        for i in range(32)[::-1]:
            prefix = set([x >> i for x in nums])
            res <<= 1
            candidate = res ^ 1
            for p in prefix:
                if candidate ^ p in prefix:
                    res = candidate
                    break
        return res

def main():
    sol = Solution()
    print(sol.findMaximumXOR([3,10,5,25,2,8]))
    print(sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))

if __name__ == '__main__':
    main()