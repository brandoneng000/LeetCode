from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        cur = 0

        for val in values:
            res = max(res, cur + val)
            cur = max(cur, val) - 1

        return res

    # def maxScoreSightseeingPair(self, values: List[int]) -> int:
    #     res = 0

    #     for i in range(len(values)):
    #         for j in range(i + 1, len(values)):
    #             res = max(res, values[i] + values[j] + i - j)
        
    #     return res

def main():
    sol = Solution()
    print(sol.maxScoreSightseeingPair([8,1,5,2,6]))
    print(sol.maxScoreSightseeingPair([1,2]))

if __name__ == '__main__':
    main()