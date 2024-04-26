from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cur = grid[0]

        for i in range(1, n):
            next = [float('inf')] * n
            
            for j in range(n):
                temp = float('inf')

                for k in range(n):
                    if j != k:
                        temp = min(temp, grid[i][j] + cur[k])
                next[j] = temp

            cur = next
        
        return min(cur)
        
def main():
    sol = Solution()
    print(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.minFallingPathSum([[1,2],[4,5]]))
    print(sol.minFallingPathSum([[7]]))

if __name__ == '__main__':
    main()