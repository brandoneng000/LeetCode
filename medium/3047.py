from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0

        for i in range(n):
            first_bl = bottomLeft[i]
            first_tr = topRight[i]

            for j in range(i + 1, n):
                second_bl = bottomLeft[j]
                second_tr = topRight[j]

                if second_bl[0] >= first_tr[0] or second_tr[0] <= first_bl[0]:
                    continue

                if second_tr[1] <= first_bl[1] or second_bl[1] >= first_tr[1]:
                    continue

                point_ax = max(first_bl[0], second_bl[0])
                point_ay = max(first_bl[1], second_bl[1])
                point_bx = min(first_tr[0], second_tr[0])
                point_by = min(first_tr[1], second_tr[1])
                side_x = point_bx - point_ax
                side_y = point_by - point_ay
                res = max(res, min(side_x, side_y))         
            
        return res * res


        
def main():
    sol = Solution()
    print(sol.largestSquareArea(bottomLeft = [[2,2],[1,3]], topRight = [[3,4],[5,5]]))
    print(sol.largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]))
    print(sol.largestSquareArea(bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]))
    print(sol.largestSquareArea(bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]))
    print(sol.largestSquareArea(bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]))

if __name__ == '__main__':
    main()