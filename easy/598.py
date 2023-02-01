from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        
        row = m
        col = n

        for op in ops:
            if op[0] < row:
                row = op[0]
            if op[1] < col:
                col = op[1]

        return row * col

def main():
    sol = Solution()
    print(sol.maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))
    print(sol.maxCount(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
    print(sol.maxCount(m = 3, n = 3, ops = []))


if __name__ == '__main__':
    main()