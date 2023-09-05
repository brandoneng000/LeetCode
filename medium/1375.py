from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = res = 0

        for i, bit in enumerate(flips, 1):
            right = max(right, bit)
            res += right == i
        
        return res

    # def numTimesAllBlue(self, flips: List[int]) -> int:
    #     n = len(flips)
    #     mask = (2 ** n) - 1
    #     cur = 0
    #     res = 0

    #     for index, bit in enumerate(flips):
    #         cur |= (1 << (n - bit))
    #         # temp = (mask & (mask << (n - index - 1)))
    #         # temp_bin = bin(temp)
    #         if cur == (mask & (mask << (n - index - 1))):
    #             res += 1

    #     return res
        
def main():
    sol = Solution()
    print(sol.numTimesAllBlue([3,2,4,1,5]))
    print(sol.numTimesAllBlue([4,1,2,3]))

if __name__ == '__main__':
    main()