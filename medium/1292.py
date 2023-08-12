from typing import List
import itertools

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i, j in itertools.product(range(m), range(n)):
            prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + mat[i][j]
        
        def check_threshold(k: int):
            for i, j in itertools.product(range(m + 1 - k), range(n + 1 - k)):
                if prefix[i + k][j + k] - prefix[i][j + k] - prefix[i - k][j] + prefix[i][j] <= threshold:
                    return True
            return False
        
        low, high = 1, min(m, n)
        while low <= high:
            middle = (low + high) // 2
            if check_threshold(middle):
                low = middle + 1
            else:
                high = middle - 1
        
        return high


def main():
    sol = Solution()
    print(sol.maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
    print(sol.maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))

if __name__ == '__main__':
    main()