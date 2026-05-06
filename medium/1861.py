from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["" for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = boxGrid[j][i]
        
        for i in range(n):
            res[i].reverse()

        for j in range(m):
            lowest_row = n - 1

            for i in range(n - 1, -1, -1):
                if res[i][j] == '#':
                    res[i][j] = '.'
                    res[lowest_row][j] = '#'
                    lowest_row -= 1

                if res[i][j] == '*':
                    lowest_row = i - 1
        
        return res
                

    # def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    #     m, n = len(box), len(box[0])
    #     res = [['.' for j in range(m)] for i in range(n)]

    #     for i in range(m):
    #         stones = 0
    #         for j in range(n):
    #             if box[i][j] == '#':
    #                 stones += 1
    #             elif box[i][j] == '*':
    #                 res[j][m - i - 1] = '*'
    #                 for s in range(stones):
    #                     res[j - s - 1][m - i - 1] = '#'
    #                 stones = 0
    #         else:
    #             for s in range(stones):
    #                 res[j - s][m - i - 1] = '#'
        
    #     return res
        
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