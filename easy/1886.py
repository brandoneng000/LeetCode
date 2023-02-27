from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        size = len(mat)

        for _ in range(4):
            for row in range(size // 2):
                for col in range(row, size - row - 1):
                    temp = mat[row][col]
                    mat[row][col] = mat[size - 1 - col][row]
                    mat[size - 1 - col][row] = mat[size - 1 - row][size - 1 - col]
                    mat[size - 1 - row][size - 1 - col] = mat[col][size - 1 - row]
                    mat[col][size - 1 - row] = temp
            if mat == target:
                return True
        
        return False
        
        

def main():
    sol = Solution()
    print(sol.findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]))
    print(sol.findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]))
    print(sol.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))

if __name__ == '__main__':
    main()