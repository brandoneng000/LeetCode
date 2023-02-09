from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        from math import isclose
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]

        if run == 0:
            x = coordinates[1][0]
            for coord in coordinates:
                if x != coord[0]:
                    return False
        else:
            slope = rise / run
            b = coordinates[0][1] - slope * coordinates[0][0]
            for coord in coordinates:
                if not isclose(slope * coord[0] + b, coord[1]):
                    return False

        return True

def main():
    sol = Solution()
    print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
    print(sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))

if __name__ == '__main__':
    main()