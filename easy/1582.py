from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = []
        result = 0

        for index in range(len(mat[0])):
            temp = []
            for j in range(len(mat)):
                temp.append(mat[j][index])
            cols.append(temp)
        
        for row in mat:
            if sum(row) == 1:
                if sum(cols[row.index(1)]) == 1:
                    result += 1
        
        return result


def main():
    sol = Solution()
    print(sol.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
    print(sol.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
    print(sol.numSpecial([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
    print(sol.numSpecial([[0,0],[0,0],[1,0]]))

if __name__ == '__main__':
    main()