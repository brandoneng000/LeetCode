from typing import List
import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        data = collections.defaultdict(int)

        for row in matrix:
            data[tuple(row)] += 1
            data[tuple(1 - val for val in row)] += 1
        
        return max(data.values())

def main():
    sol = Solution()
    print(sol.maxEqualRowsAfterFlips([[0,1],[1,1]]))
    print(sol.maxEqualRowsAfterFlips([[0,1],[1,0]]))
    print(sol.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))

if __name__ == '__main__':
    main()