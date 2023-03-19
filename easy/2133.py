from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        total = len(matrix) * (len(matrix) + 1) // 2
        rows = [0] * len(matrix)
        cols = [0] * len(matrix)
        nums = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                nums.add(matrix[r][c])
                # rows[r] += matrix[r][c]
                # cols[c] += matrix[r][c]
            
            if len(nums) != len(matrix):
                return False
            nums.clear()
        
        # return all(total == row for row in rows) and all(total == col for col in cols)
        return True

def main():
    sol = Solution()
    print(sol.checkValid([[1,2,3],[3,1,2],[2,3,1]]))
    print(sol.checkValid([[1,1,1],[1,2,3],[1,2,3]]))
    print(sol.checkValid([[2,2,2],[2,2,2],[2,2,2]]))
    print(sol.checkValid([[4,2,2,2],[1,1,4,4],[3,3,1,3],[2,4,3,1]]))

if __name__ == '__main__':
    main()