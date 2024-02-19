from typing import List
from collections import deque

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        cur = [0]

        for row in mat:
            next = set()

            for cur_val in cur:
                for add_val in set(row):
                    next.add(cur_val + add_val)
            
            cur = list(next)
            

        return min(abs(target - val) for val in cur)
        
        
def main():
    sol = Solution()
    print(sol.minimizeTheDifference(mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13))
    print(sol.minimizeTheDifference(mat = [[1],[2],[3]], target = 100))
    print(sol.minimizeTheDifference(mat = [[1,2,9,8,7]], target = 6))

if __name__ == '__main__':
    main()