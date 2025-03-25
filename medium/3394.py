from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = []
        vertical = []

        for start_x, start_y, end_x, end_y in rectangles:
            horizontal.append([start_x, end_x])
            vertical.append([start_y, end_y])
        
        horizontal.sort()
        vertical.sort()
        cur_end_x = horizontal[0][1]
        cur_end_y = vertical[0][1]
        count_x_rect = 0
        count_y_rect = 0

        for i in range(len(horizontal)):
            start_x, end_x = horizontal[i]
            start_y, end_y = vertical[i]

            if start_x >= cur_end_x:
                count_x_rect += 1
            cur_end_x = max(cur_end_x, end_x)

            if start_y >= cur_end_y:
                count_y_rect += 1
            cur_end_y = max(cur_end_y, end_y)
        
        return count_x_rect >= 2 or count_y_rect >= 2

        
def main():
    sol = Solution()
    print(sol.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
    print(sol.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
    print(sol.checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))

if __name__ == '__main__':
    main()