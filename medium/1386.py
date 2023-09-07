from typing import List
import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 2 * n
        occupied = collections.defaultdict(set)
        valid = [{2, 3, 4, 5}, {6, 7, 8, 9}, {4, 5, 6, 7}]

        for row, seat in reservedSeats:
            for i, v in enumerate(valid):
                if seat in v:
                    occupied[row].add(i)
        
        for row in occupied:
            if len(occupied[row]) == 3:
                res -= 2
            else:
                res -= 1

        return res

    # def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    #     res = 0
    #     occupied = collections.defaultdict(set)
    #     valid = [{2, 3, 4, 5}, {6, 7, 8, 9}, {4, 5, 6, 7}]
        
    #     for row, seat in reservedSeats:
    #         occupied[row].add(seat)
        
    #     for row in range(1, n + 1):
    #         aisle = not occupied[row] & valid[0]
    #         aisle += not occupied[row] & valid[1]
    #         inner = not occupied[row] & valid[2]

    #         res += max(aisle, inner)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    print(sol.maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
    print(sol.maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))

if __name__ == '__main__':
    main()