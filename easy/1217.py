from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0

        for chip in position:
            if chip % 2:
                odds += 1

        return min(odds, len(position) - odds)
        

def main():
    sol = Solution()
    print(sol.minCostToMoveChips([1,2,3]))
    print(sol.minCostToMoveChips([2,2,2,3,3]))
    print(sol.minCostToMoveChips([1,1000000000]))
    print(sol.minCostToMoveChips([6,4,7,8,2,10,2,7,9,7]))

if __name__ == '__main__':
    main()