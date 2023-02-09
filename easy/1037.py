from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        from math import isclose 
        first = tuple(points[0])
        second = tuple(points[1])
        third = tuple(points[2])

        if first == second or first == third or second == third:
            return False
        
        rise = second[1] - first[1]
        run = second[0] - first[0]
        slope = rise / run if run else float('inf')
        rise = third[1] - first[1]
        run = third[0] - first[0]

        return not isclose(slope, rise / run if run else float('inf'))



def main():
    sol = Solution()
    print(sol.isBoomerang([[1,1],[2,3],[3,2]]))
    print(sol.isBoomerang([[1,1],[2,2],[3,3]]))

if __name__ == '__main__':
    main()