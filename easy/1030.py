from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result = []

        for row in range(rows):
            for col in range(cols):
                result.append([row, col])
        
        return sorted(result, key = lambda x: abs(rCenter - x[0]) + abs(cCenter - x[1]))

def main():
    sol = Solution()
    print(sol.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))
    print(sol.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))
    print(sol.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2))

if __name__ == '__main__':
    main()