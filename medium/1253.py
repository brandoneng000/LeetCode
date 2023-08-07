from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        n = len(colsum)
        res = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []

        for i in range(n):
            if colsum[i] == 0 or colsum[i] == 2:
                continue
            else:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    res[1][i] = 1
                    lower -= 1
        
        return res


def main():
    sol = Solution()
    print(sol.reconstructMatrix(upper = 3, lower = 1, colsum = [2,1,1]))
    print(sol.reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
    print(sol.reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
    print(sol.reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))

if __name__ == '__main__':
    main()