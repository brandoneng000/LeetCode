from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [['.' for j in range(m)] for i in range(n)]

        for i in range(m):
            stones = 0
            for j in range(n):
                if box[i][j] == '#':
                    stones += 1
                elif box[i][j] == '*':
                    res[j][m - i - 1] = '*'
                    for s in range(stones):
                        res[j - s - 1][m - i - 1] = '#'
                    stones = 0
            else:
                for s in range(stones):
                    res[j - s][m - i - 1] = '#'
        
        return res
        
def main():
    sol = Solution()
    print(sol.rotateTheBox([["#",".","#"]]))
    print(sol.rotateTheBox([["#",".","*","."],
                            ["#","#","*","."]]))
    print(sol.rotateTheBox([["#","#","*",".","*","."],
                            ["#","#","#","*",".","."],
                            ["#","#","#",".","#","."]]))

if __name__ == '__main__':
    main()