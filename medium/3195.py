from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = top = float('inf')
        right = bottom = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i < top:
                        top = i
                    
                    if j < left:
                        left = j

                    if j > right:
                        right = j
                        
                    bottom = i
                    
        
        width = right - left + 1
        height = bottom - top + 1

        return width * height
        
        
def main():
    sol = Solution()
    print(sol.minimumArea([[0,0,0],[0,0,0],[0,0,1],[0,1,0]]))
    print(sol.minimumArea([[0,1,0],[1,0,1]]))
    print(sol.minimumArea([[1,0],[0,0]]))

if __name__ == '__main__':
    main()