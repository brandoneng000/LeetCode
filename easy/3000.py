from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        max_diag = 0

        for l, w in dimensions:
            diag = l * l + w * w

            if diag > max_diag:
                res = l * w
                max_diag = diag
            elif diag == max_diag:
                res = max(res, l * w)
        
        return res

        
def main():
    sol = Solution()
    print(sol.areaOfMaxDiagonal([[9,3],[8,6]]))
    print(sol.areaOfMaxDiagonal([[3,4],[4,3]]))

if __name__ == '__main__':
    main()