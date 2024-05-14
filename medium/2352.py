from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        transpose = [[grid[j][i] for j in range(n)] for i in range(n)]
        res = 0

        for i in range(n):
            for j in range(n):
                res += grid[i] == transpose[j]
        
        return res
                
        
def main():
    sol = Solution()
    print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
    print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

if __name__ == '__main__':
    main()