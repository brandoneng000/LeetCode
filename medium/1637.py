from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = sorted(set([x for x, y in points]))
        res = 0

        for i in range(len(x_axis) - 1):
            res = max(res, x_axis[i + 1] - x_axis[i])
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
    print(sol.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))

if __name__ == '__main__':
    main()