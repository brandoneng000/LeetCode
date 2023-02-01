from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        new_matrix_row = []
        c_count = 0
        
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        for row in mat:
            for col in row:
                new_matrix_row.append(col)
                c_count += 1
                if c_count == c:
                    result.append(new_matrix_row)
                    c_count = 0
                    new_matrix_row = []
        
        return result


def main():
    sol = Solution()
    print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
    print(sol.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))

if __name__ == '__main__':
    main()