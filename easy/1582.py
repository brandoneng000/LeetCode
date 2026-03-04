from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        res = 0

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        res += 1
        
        return res

    # def numSpecial(self, mat: List[List[int]]) -> int:
    #     cols = []
    #     result = 0

    #     for index in range(len(mat[0])):
    #         temp = []
    #         for j in range(len(mat)):
    #             temp.append(mat[j][index])
    #         cols.append(temp)
        
    #     for row in mat:
    #         if sum(row) == 1:
    #             if sum(cols[row.index(1)]) == 1:
    #                 result += 1
        
    #     return result


def main():
    sol = Solution()
    print(sol.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
    print(sol.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
    print(sol.numSpecial([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
    print(sol.numSpecial([[0,0],[0,0],[1,0]]))

if __name__ == '__main__':
    main()