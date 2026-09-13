from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_pnts = []
        img2_pnts = []
        diff = defaultdict(int)

        for r in range(n):
            for c  in range(n):
                if img1[r][c]:
                    img1_pnts.append((r, c))

                if img2[r][c]:
                    img2_pnts.append((r, c))

        for r1, c1 in img1_pnts:
            for r2, c2 in img2_pnts:
                diff[(r2 - r1, c2 - c1)] += 1

        return max(diff.values() or [0])

    # def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
    #     n = len(img1)

    #     def helper(r_shift: int, c_shift: int, moved: List[List[int]], static: List[List[int]]):
    #         left, right = 0, 0
    #         for r_row, m_row in enumerate(range(r_shift, n)):
    #             for r_col, m_col in enumerate(range(c_shift, n)):
    #                 if moved[m_row][m_col] == 1 and moved[m_row][m_col] == static[r_row][r_col]:
    #                     left += 1
    #                 if moved[m_row][r_col] == 1 and moved[m_row][r_col] == static[r_row][m_col]:
    #                     right += 1
            
    #         return max(left, right)

    #     res = 0
    #     for i in range(n):
    #         for j in range(n):
    #             res = max(res, helper(i, j, img1, img2))
    #             res = max(res, helper(i, j, img2, img1))
        
    #     return res

def main():
    sol = Solution()
    print(sol.largestOverlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))
    print(sol.largestOverlap(img1 = [[1]], img2 = [[1]]))
    print(sol.largestOverlap(img1 = [[0]], img2 = [[0]]))

if __name__ == '__main__':
    main()