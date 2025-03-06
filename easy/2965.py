from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        valid_nums = set([i for i in range(1, n * n + 1)])
        repeating = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] in valid_nums:
                    valid_nums.discard(grid[i][j])
                else:
                    repeating = grid[i][j]
        
        return [repeating, valid_nums.pop()]
        
def main():
    sol = Solution()
    print(sol.findMissingAndRepeatedValues([[1,3],[2,2]]))
    print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))

if __name__ == '__main__':
    main()