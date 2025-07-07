from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(0, 2):
            for col in range(0, 2):
                black_count = 0
                black_count += grid[row][col] == 'B'
                black_count += grid[row][col + 1] == 'B'
                black_count += grid[row + 1][col + 1] == 'B'
                black_count += grid[row + 1][col] == 'B'
            
                if black_count <= 1 or black_count >= 3:
                    return True
        
        return False

        
def main():
    sol = Solution()
    print(sol.canMakeSquare(grid = [["B","W","B"],["B","W","W"],["B","W","B"]]))
    print(sol.canMakeSquare(grid = [["B","W","B"],["W","B","W"],["B","W","B"]]))
    print(sol.canMakeSquare(grid = [["B","W","B"],["B","W","W"],["B","W","W"]]))

if __name__ == '__main__':
    main()