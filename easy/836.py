from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # corners should overlap in rect
        A, B, C, D = rec1[0], rec1[1], rec1[2], rec1[3]
        E, F, G, H = rec2[0], rec2[1], rec2[2], rec2[3]

        # get the overlapping corners if there are any
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        return x1 < x2 and y1 < y2


def main():
    sol = Solution()
    print(sol.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
    print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
    print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))
    print(sol.isRectangleOverlap(rec1 = [5,15,8,18], rec2 = [0,3,7,9]))

if __name__ == '__main__':
    main()