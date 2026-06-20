from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions
        r.append([1, 0])
        r.sort()

        if r[-1][0] != n:
            r.append([n, n - 1])
        
        m = len(r)
        res = 0

        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        
        for i in range(m - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))
        
        for i in range(m - 1):
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            res = max(res, best)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxBuilding(n = 5, restrictions = [[2,1],[4,1]]))
    print(sol.maxBuilding(n = 6, restrictions = []))
    print(sol.maxBuilding(n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]))

if __name__ == '__main__':
    main()