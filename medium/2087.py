from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res = 0
        [i, j] = homePos

        while i != startPos[0]:
            res += rowCosts[i]
            i += -1 if i > startPos[0] else 1
        while j != startPos[1]:
            res += colCosts[j]
            j += -1 if j > startPos[1] else 1
        
        return res


        
def main():
    sol = Solution()
    print(sol.minCost(startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]))
    print(sol.minCost(startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]))

if __name__ == '__main__':
    main()