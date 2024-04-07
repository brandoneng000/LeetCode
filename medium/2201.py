from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0 for j in range(n)] for i in range(n)]
        res = 0

        for r, c in dig:
            grid[r][c] = 1
        
        for r1, c1, r2, c2 in artifacts:
            artifact = 1

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    artifact &= grid[r][c]
            
            res += artifact
        
        return res
        

def main():
    sol = Solution()
    print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]))
    print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]))

if __name__ == '__main__':
    main()