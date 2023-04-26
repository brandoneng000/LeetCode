from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        res = 0
        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            res += max(temp)
        
        return res

def main():
    sol = Solution()
    print(sol.deleteGreatestValue([[1,2,4],[3,3,1]]))
    print(sol.deleteGreatestValue([[10]]))

if __name__ == '__main__':
    main()