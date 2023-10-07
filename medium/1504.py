from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i - 1][j]
        
        res = 0
        for i in range(m):
            stack = []
            count = 0

            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    count -= (mat[i][jj] - mat[i][j]) * (jj - kk)

                count += mat[i][j]
                res += count
                stack.append(j)
        
        return res
            

        
def main():
    sol = Solution()
    print(sol.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
    print(sol.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]))

if __name__ == '__main__':
    main()